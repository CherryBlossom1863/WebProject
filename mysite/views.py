from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.db import models
import requests

from mysite.apps.comments.models import Comment
from mysite.apps.articles.models import Article
from mysite.forms import UserRegisterForm, UserLogInForm, CommentInputForm


def index(request):
  return HttpResponseRedirect('news/')

def auth_page(request):
  if request.method == 'POST':
    form = UserLogInForm(request.POST)
    if form.is_valid():
        return HttpResponseRedirect('/')
  else:
    t = get_template('section.auth.html')
    form = UserLogInForm()
    mdict = {'Title':'Log in', 'form':form}
    mdict.update(csrf(request))
    html = t.render(mdict)
  return HttpResponse(html)


def auth_register_page(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()#request.user
    return HttpResponseRedirect('/')
  else:
    t = get_template('section.auth.register.html')
    form = UserRegisterForm()
    mdict = {'Title':'Register', 'form':form}
    mdict.update(csrf(request))
    html = t.render(mdict)
  return HttpResponse(html)

def section_page(request):
  #request to API
  url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
  myobj = {'api-key': 'k4RmVAZGBrKDDr3AwJS7i6oBfSRyAhmb'}
  req = requests.post(url, params = myobj).json()
  if(req['status'] != 'OK'):
    req = requests.post(url, params = myobj).json()

  #Saving new articles to DB
  for article in req['response']['docs']:
    try:
      ref = "/articles/" + str(article['web_url']).split("/",3)[-1]
      Article.objects.filter(url = ref).get()
    except Article.DoesNotExist:
      art = Article()
      art.the_json = article
      art.url = ref
      art.save()
    
  #page render
  t = get_template('section.base.html')
  title = str(request.path).split("/")[-2]
  title = str.capitalize(title)
  mdict = {'Title':title, 'inf_list':req['response']['docs'],}
  mdict.update(csrf(request))
  html = t.render(mdict)
  return HttpResponse(html)

def article_page(request):
  #request to DB for an article
  ref = '/articles/2022/06/13/business/what-you-should-know-about-bear-markets.html'
  #str(request.path).split("/",3)[-1]
  article = Article.objects.filter(url = ref).get(pk=1).the_json
  #Comments input form
  form = CommentInputForm()

  #Comments tree request to DB
  comments = []
  web_url = article['web_url']
  try:
    com_list = Comment.objects.filter(url = web_url).order_by('creation_date')
    for com in com_list:
      comments.append(com)
  except Comment.DoesNotExist:
    pass
    #TODO: no comments

  #page render
  t = get_template('section.base.html')
  title = str(request.path).split("/")[-2]
  title = str.capitalize(title)
  mdict = {'Title':title, 'inf_list':article['response']['docs'], 'form':form}
  mdict.update(csrf(request))
  html = t.render(mdict)
  return HttpResponse(html)

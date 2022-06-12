from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.db import models
import requests

from mysite.apps.comments.models import Comment
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
  if request.method == 'POST':
    form = CommentInputForm(request.POST)
    if form.is_valid():
      form.save()
    return HttpResponseRedirect('/')
  else:
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    myobj = {'api-key': 'k4RmVAZGBrKDDr3AwJS7i6oBfSRyAhmb'}
    req = requests.post(url, params = myobj).json()
    if(req['status'] != 'OK'):
      req = requests.post(url, params = myobj).json()

    #Comments input form
    form = CommentInputForm()

    #Comments tree request to DB
    comments_ = []
    for dict in req['response']['docs']:
      web_url_ = dict['web_url']
      try:
        com_list_ = Comment.objects.filter(post = web_url_).get()
      except Comment.DoesNotExist:
        com_list_ = []
      comments_.append(com_list_)
    
    t = get_template('section.base.html')
    title = str(request.path).split("/")[-2]
    title = str.capitalize(title)
    mdict = {'Title':title, 'inf_list':req['response']['docs'], 'form':form}
    mdict.update(csrf(request))
    html = t.render(mdict)
  return HttpResponse(html)

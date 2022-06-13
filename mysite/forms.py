from django import forms

from mysite.apps.users.models import User
from mysite.apps.comments.models import Comment


class UserRegisterForm(forms.ModelForm):
  class Meta:
        model = User
        fields = ['login','password','email','name','surname',]
  login = forms.CharField(label="login", required=True)
  email=forms.EmailField(label="Email", widget=forms.EmailInput, required=True)
  password=forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
  name=forms.CharField(label="Name", required=True)
  surname=forms.CharField(label="Surname", required=True)

class UserLogInForm(forms.Form):
  login=forms.EmailField(label="Email", required=True)
  password=forms.CharField(label="Password",widget=forms.PasswordInput, required=True)

class CommentInputForm(forms.ModelForm):
  class Meta:
        model = Comment
        fields = ['content',]
  content = forms.CharField(label="", required=True, widget=forms.Textarea)

    
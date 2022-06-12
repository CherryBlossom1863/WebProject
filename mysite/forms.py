from django import forms
from mysite.apps.users.models import User
from mysite.apps.comments.models import Comment


class UserRegisterForm(forms.ModelForm):
  class Meta:
        model = User
        fields = ['name','surname','age','login','password', 'birth_date',]
  name=forms.CharField(label="Name", required=True)
  surname=forms.CharField(label="Surname", required=True)
  age=forms.IntegerField(label="Age", required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'min': 0, 'max': 110}))
  login=forms.EmailField(label="Email", required=True)
  password=forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
  birth_date=forms.DateField(label="Birth Date", required=False)

class UserLogInForm(forms.Form):
  login=forms.EmailField(label="Email", required=True)
  password=forms.CharField(label="Password",widget=forms.PasswordInput, required=True)

class CommentInputForm(forms.ModelForm):
  class Meta:
        model = Comment
        fields = ['content',]
  content = forms.CharField(label="", required=True)
    
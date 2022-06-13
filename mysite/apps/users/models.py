from django.db import models

class User(models.Model):
  login = models.CharField(max_length=30)
  password=models.CharField(max_length=30)
  email=models.EmailField(default="unknown@a.ru")
  name=models.CharField(max_length=30)
  surname=models.CharField(max_length=30)
  
  def __unicode__(self):
    return self.name


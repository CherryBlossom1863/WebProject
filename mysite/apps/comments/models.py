from django.db import models
import datetime

class Comment(models.Model):
  login=models.EmailField(default="anonymous")
  post=models.URLField(max_length=200)
  creation_date=models.DateField(default=datetime.datetime.now())
  content=models.CharField(max_length=500)
  
  
  def __unicode__(self):
    return self.name

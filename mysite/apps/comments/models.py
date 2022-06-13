from django.db import models
from django.utils.timezone import now

class Comment(models.Model):
  login=models.CharField(max_length=200, default='anonymous')
  url=models.TextField(max_length=200, blank=True)
  creation_date=models.DateField(default = now())
  content=models.TextField(max_length=500)
  
  
  def __unicode__(self):
    return self.name

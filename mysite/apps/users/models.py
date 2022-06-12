from django.db import models

class User(models.Model):
  name=models.CharField(max_length=30)
  surname=models.CharField(max_length=30)
  age=models.IntegerField(default=0)
  login=models.EmailField()
  password=models.CharField(max_length=30)
  birth_date=models.DateField(default="1970-01-01")
  
  def __unicode__(self):
    return self.name


from django.db import models
import jsonfield


class Article(models.Model):
  the_json = jsonfield.JSONField()
  url = models.TextField(max_length=200, blank=True)

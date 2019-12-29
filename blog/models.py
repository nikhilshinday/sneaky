from django.db import models


class Blog(models.Model):
    text = models.TextField()
    url_title = models.CharField(max_length=20)
    title = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    views = models.IntegerField(default=0)

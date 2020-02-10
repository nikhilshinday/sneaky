from django.db import models


class Blog(models.Model):
    text = models.TextField()
    url_title = models.CharField(max_length=20)
    title = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    views = models.IntegerField(default=0)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
    read_ts = models.DateField()


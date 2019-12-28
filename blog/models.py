from django.db import models


class Blog(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    views = models.IntegerField(default=0)

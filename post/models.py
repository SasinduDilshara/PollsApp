from django.db import models
import datetime
from django.utils import timezone


class Post(models.Model):
    name =models.CharField(max_length=80)
    size = models.IntegerField()
    def __str__(self):
        return self.name
    def nameOf(self):
        return self.name

class PostLike(models.Model):
    likedPost = models.OneToOneField(Post, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Hi"
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=30)


class Idea(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500, null=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Book(models.Model):
    name_book = models.CharField(max_length=100)
    description_book = models.CharField(max_length=100)
    author_book = models.CharField(max_length=100)
    file = models.FileField(upload_to='upldfile/')
    photo = models.ImageField(upload_to='photo/')

    def __str__(self):
        return self.name_book

    def get_absolute_url(self):
        return '/book/'

class Reviews(models.Model):
     nickname = models.CharField(max_length=100)
     reviews = models.TextField()


# class User(AbstractUser):
#     pass


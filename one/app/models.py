from django.db import models
from django.utils import timezone
from time import time

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20, unique=True, null=False)
    age = models.PositiveSmallIntegerField(default=0)
    phone = models.CharField(max_length=11, null=True, default="", db_index=True)
    email = models.EmailField(null=True, default="")
    info = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, default='')
    birthday = models.CharField(max_length=100, null=True, default="")


class Diary(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, related_name='diary', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    create_time = models.IntegerField()


class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ManyToManyField(User, related_name="group")
    name = models.CharField(max_length=20)
    create_time = models.IntegerField()
    update_time = models.IntegerField()


class Image(models.Model):
    image = models.ImageField()

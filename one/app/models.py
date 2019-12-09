import json
from time import localtime, strftime
from functools import wraps

from django.db import models
from django.utils import timezone
from time import time
from django_redis import get_redis_connection
from .consts import MsgType


_cache = get_redis_connection("default")


def cache(func):
    @wraps(func)
    def wrapper(obj, *args):
        print(args)
        key = args[0]
        value = _cache.get(key)
        if value:
            print("got it!")
            return json.loads(value)
        rs = func(obj, *args)
        _cache.set(key, json.dumps(rs))
        return rs
    return wrapper

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True, null=False)
    age = models.PositiveSmallIntegerField(default=0)
    phone = models.CharField(max_length=11, null=True, default="", db_index=True)
    email = models.EmailField(null=True, default="")
    info = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        index_together = ['username', 'phone']

    def __str__(self):
        return 'user:{}'.format(self.username)

    @classmethod
    @cache
    def get(cls, id):
        rs = cls.objects.get(id=id)
        return {
            "id": rs.id,
            "username": rs.username,
            "age": rs.age,
            "phone": rs.phone,
            "email": rs.email,
            "info": rs.info,
            "create_time": str(rs.create_time),
            "update_time": str(rs.update_time)
        }


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, default='')
    birthday = models.CharField(max_length=100, null=True, default="")


class Diary(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='diary', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    create_time = models.IntegerField()


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ManyToManyField(User, related_name="group")
    name = models.CharField(max_length=20)
    create_time = models.IntegerField()
    update_time = models.IntegerField()


class Image(models.Model):
    image = models.ImageField()


class Message(models.Model):
    content = models.TextField()
    message_type = models.CharField(max_length=10, db_index=True)
    created_time = models.IntegerField(default=0)

    def __str__(self):
        return "type: %s, content: %s" % (self.message_type, self.content)

    @property
    def msg_type(self):
        try:
            return MsgType[self.message_type]
        except KeyError:
            return MsgType.info

    @property
    def get_time(self):
        return strftime("%Y-%m-%d %H:%M:%S", localtime(self.created_time))

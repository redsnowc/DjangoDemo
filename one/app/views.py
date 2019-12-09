# coding:utf-8
import time

from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import HttpResponse
from django.http import JsonResponse
from .mako_render import mako_render
from .consts import MsgType
from django_redis import get_redis_connection
from .models import Message

# Create your views here.


def index(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    print(request.META)
    cache = get_redis_connection('default')
    cache.set("test", "redsnow")
    print(cache.get("test"))
    return HttpResponse("Hello World %s, you are %s years old" % (name, age))


def args(request, name, age):
    return HttpResponse("Hello World %s, you are %s years old" % (name, age))


def ajax(request):
    return JsonResponse({"a": 1})


class Two(View):
    def get(self, request):
        return HttpResponse("This is a class view test.")


def loop(request):
    data = {"array": range(1, 11)}
    return render(request, "app/index.html", data)


def test_jinja(request):
    data = {"num": 10, "array": [1, 2, 3]}
    return render(request, "app/jinja.html", data)


class TestMako(View):
    TEMPLATE = "app/mako.html"

    def get(self, request):
        data = {"name": "tom", "age": 18}
        return mako_render(request, self.TEMPLATE, data=data)


# class Message(View):
#     TEMPLATE = "app/message.html"
#
#     def get(self, request, msg_type):
#         data = {}
#
#         try:
#             msg_type_obj = MsgType[msg_type]
#         except KeyError:
#             data["error"] = "没有这个消息类型"
#             return render(request, self.TEMPLATE, data)
#
#         msg = request.GET.get("msg", "")
#         if not msg:
#             data["error"] = "消息不可为空"
#             return render(request, self.TEMPLATE, data)
#
#         data["msg"] = msg
#         data["msg_type"] = msg_type_obj
#
#         return render(request, self.TEMPLATE, data)


class L1(View):
    Template = "app/l1.html"

    def get(self, request, message_type):
        data = {}

        try:
            message_type_obj = MsgType[message_type]
        except Exception as e:
            data['error'] = "没有这个消息类型 %s" % e
            return render(request, self.Template, data)

        message = request.GET.get('message', '')
        if not message:
            data['error'] = '消息不可为空'
            return render(request, self.Template, data)

        Message.objects.create(content=message, message_type=message_type,
                               created_time=time.time())

        return redirect(reverse("app:l2"))


class L2(View):
    TEMPLATE = 'app/l2.html'

    def get(self, request):
        data = {}
        like = request.GET.get('search', '')
        if like:
            messages = Message.objects.filter(content__contains=like)
        else:
            messages = Message.objects.all()
        data['messages'] = messages
        return render(request, self.TEMPLATE, data)


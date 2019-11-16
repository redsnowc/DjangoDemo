# coding:utf-8
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.http import JsonResponse
from .mako_render import mako_render

# Create your views here.


def index(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    print(request.META)
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
    data = {}
    data["num"] = 10
    data["array"] = [1, 2, 3]
    return render(request, "app/jinja.html", data)


class TestMako(View):
    TEMPLATE = "app/mako.html"

    def get(self, request):
        data = {"name": "tom", "age": 18}
        return mako_render(request, self.TEMPLATE, data=data)


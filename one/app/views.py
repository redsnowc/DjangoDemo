# coding:utf-8
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.http import JsonResponse

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


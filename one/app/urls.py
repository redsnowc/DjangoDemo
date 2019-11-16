from django.urls import path

from .views import index, args, ajax, Two, loop, test_jinja, TestMako

app_name = "app"
urlpatterns = [
    path('', index, name="index"),
    path('args/<str:name>/<int:age>', args),
    path('ajax', ajax),
    path('two', Two.as_view()),
    path('loop', loop),
    path('jinja', test_jinja),
    path('mako', TestMako.as_view()),
]

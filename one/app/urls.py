from django.urls import path

from .views import index, args, ajax, Two, loop, test_jinja, TestMako, L1, L2

app_name = "app"
urlpatterns = [
    path('', index, name="index"),
    path('args/<str:name>/<int:age>', args),
    path('ajax', ajax),
    path('two', Two.as_view()),
    path('loop', loop),
    path('jinja', test_jinja),
    path('mako', TestMako.as_view()),
    # path('msg/<str:msg_type>', Message.as_view(), name="msg"),
    path('l1/<str:message_type>', L1.as_view()),
    path('l2', L2.as_view(), name="l2")
]

from django.urls import path

from .views import index, args, ajax, Two

urlpatterns = [
    path('', index),
    path('args/<str:name>/<int:age>', args),
    path('ajax', ajax),
    path('two', Two.as_view())
]

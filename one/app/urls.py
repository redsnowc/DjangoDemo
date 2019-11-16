from django.urls import path

from .views import index, args, ajax, Two, loop

app_name = "app"
urlpatterns = [
    path('', index, name="index"),
    path('args/<str:name>/<int:age>', args),
    path('ajax', ajax),
    path('two', Two.as_view()),
    path('loop', loop)
]

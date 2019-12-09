from django import template
from time import localtime, strftime

register = template.Library()


@register.filter
def do_something(value, args):
    return args + str(value)


@register.filter(name="test")
def again(value):
    return value + "1"


@register.filter
def sw_time(value):
    return strftime("%Y-%m-%d %H:%M:%S", localtime(value))

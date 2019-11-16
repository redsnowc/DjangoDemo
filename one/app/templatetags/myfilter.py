from django import template

register = template.Library()


@register.filter
def do_something(value, args):
    return args + str(value)


@register.filter(name="test")
def again(value):
    return value + "1"

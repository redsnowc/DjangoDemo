from jinja2 import Environment
from django.templatetags.static import static
# from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from .myfilter import for_test


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        "static": static,
        # "static": staticfiles_storage,
        "url": reverse
    })
    env.filters["for_test"] = for_test
    return env

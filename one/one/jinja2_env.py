from jinja2 import Environment
from django.templatetags.static import static
# from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from .myfilter import for_test, sensitive_word_filter, switch_timestamp


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        "static": static,
        # "static": staticfiles_storage,
        "url": reverse
    })
    env.filters["for_test"] = for_test
    env.filters["sw_filter"] = sensitive_word_filter
    env.filters["sw_time"] = switch_timestamp
    return env

from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()


@register.filter(name='split_string')
@stringfilter
def split_string(string_value, character):
    return f"{character}".join(list(string_value))

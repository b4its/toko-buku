from textwrap import wrap
from django import template


register = template.Library()


@register.filter
def text_wrap(text, width= 100):

    return ''.join(wrap(text, width))

@register.filter
def judul_wrap(text, width= 50):

    return ''.join(wrap(text, width))




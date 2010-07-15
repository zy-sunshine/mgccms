from django.template import Library
from django.conf import settings

register = Library()

# -----------------------------------------------
# render_content and render_tease
@register.inclusion_tag('mgccms/snippet/content.html')
def render_content(content, markup):
    return {
        'content': content,
        'markup': markup
    }

@register.inclusion_tag('mgccms/snippet/tease.html')
def render_tease(news):
    return {
        'o': news
    }

from django.template.defaultfilters import stringfilter

@register.filter
@stringfilter
def truncate_zh(value,arg):
    """
    Truncate a string including chinese characters.
    Argument:Numbers of Chinese characters to truncate after.
    """
    if len(value) < arg:
        r=range(len(value))
    else:
        r=range(arg)
    for s in r:
        if len(value[s].encode('gb18030')) == len(value[s]):
            # It is a number
            arg +=1
    try:
        number = arg
        if int(number) < len(value):
            return value[0:int(number)] + '..'
        else:
            return value
    except:
        return value

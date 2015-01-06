from django import template

register = template.Library()

@register.simple_tag
def bold_text(text):
    return '<b style="color:red;">' + text + '</b>'
from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list():
    return {'cats': Category.objects.all()}


@register.simple_tag
def bold_text(text):
    return '<b>' + text + '</b>'
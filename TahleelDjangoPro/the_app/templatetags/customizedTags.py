from django import template

register = template.Library()

@register.filter(name='ReplaceUnderScore')
def split(str):
    return str.replace("_"," " )
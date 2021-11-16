from django import template

register = template.Library()

@register.filter(name='incrementar')
def incrementar(valor):
	return int(valor)+1

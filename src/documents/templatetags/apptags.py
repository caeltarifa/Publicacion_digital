from django import template

register = template.Library()

@register.filter(name='esta_en_grupo')
def esta_en_grupo(user, nombre_grupo):
	return user.groups.filter(name=nombre_grupo).exists()


@register.filter(name='split')
def split(value, key):
    return value.split(key)
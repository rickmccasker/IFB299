from django import template
register = template.Library()

@register.filter(name = 'get_model_val')
def get_model_val(self, value):
	return self[value]
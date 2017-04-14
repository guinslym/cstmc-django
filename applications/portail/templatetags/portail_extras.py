from django import template

#from ..kiwoom import k_module

register = template.Library()
import random

#simple_tag
#inclusion_tag
#assignment_tag

@register.simple_tag
def get_options():
	options = [' color-',' check','radio', ' option']
	options[0] = options[0] + str(random.randint(1,2))
	options[1] = options[1] + str(random.randint(1,2))
	options[2] = options[2] + str(random.randint(1,3))
	options[3] = options[3] + str(random.randint(1,4))
	options = ' '.join(options)
	return options

@register.simple_tag
def get_image():
	image = ['Image ']
	image[0] = image[0] + str(random.randint(1,16))
	return image[0]

@register.filter
def get_master_code_name(code):
    result = "k_module.get_master_code_name(code)"
    return result
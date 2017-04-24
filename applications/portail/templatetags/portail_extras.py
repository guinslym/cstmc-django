from django import template
from random import shuffle

#from ..kiwoom import k_module

register = template.Library()
import random
from applications.portail.models import Artefact

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

@register.simple_tag
def get_objname():
	artefacts = Artefact.objects.all()
	art_name = [i.ObjectName for i in artefacts if len(i.ObjectName) > 1]
	art_name = list(set(art_name))
	art_name_with_milliseconds = []
	for obj in art_name:
		value = ["^400","^300","^200","^100"]
		art_name_with_milliseconds.append(value[random.randint(0,3	)] + str(obj))
	shuffle(art_name_with_milliseconds)
	return '","'.join(art_name)

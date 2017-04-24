from django import template
from random import shuffle

#from ..kiwoom import k_module

register = template.Library()
import random
from applications.portail.models import Artefact
from collections import Counter

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
	return '","'.join(art_name[:20])

@register.simple_tag
def get_materials(artefact):
	material_list_to_return = []
	if 'glass' in artefact:
		material_list_to_return.append(' option1 ')
	elif 'metal' in artefact:
		material_list_to_return.append(' option2 ')
	elif 'paper' in artefact:
		material_list_to_return.append(' option3 ')
	else:
		return 'option4'
	material_list_to_return = ''.join(material_list_to_return)
	return material_list_to_return

@register.simple_tag
def get_country(country):
	if 'United States of America' in country:
		return 'color-2'
	elif 'Canada' in country:
		return 'color-1'
	else:
		return 'othercountry'


@register.simple_tag
def get_categories(category1):
	if 'Receiving' in category1:
		return 'check1'
	elif 'Aircraft parts' in category1:
		return 'check2'
	else:
		return 'check3'

@register.simple_tag
def get_groups(artefact_group):
	if 'Aviation' in artefact_group:
		return 'radio2'
	elif 'Vacuum Tubes' in artefact_group:
		return 'radio3'
	elif 'Railway Transportation'in artefact_group:
		return 'radio4'
	else:
		return 'radio1'

#################################
@register.simple_tag
def display_materials(artefact):
	material_list_to_return = []
	if 'glass' in artefact:
		material_list_to_return.append(' glass ')
	elif 'metal' in artefact:
		material_list_to_return.append(' metal ')
	elif 'paper' in artefact:
		material_list_to_return.append(' paper ')
	else:
		return 'othermat'
	material_list_to_return = ''.join(material_list_to_return)
	return material_list_to_return

@register.simple_tag
def display_country(country):
	if 'United States of America' in country:
		return 'USA'
	elif 'Canada' in country:
		return 'Canada'
	else:
		return 'othercountry'


@register.simple_tag
def display_categories(category1):
	if 'Receiving' in category1:
		return 'Receiving'
	elif 'Aircraft parts' in category1:
		return 'Aircraft'
	else:
		return 'othercategories'

@register.simple_tag
def display_groups(artefact_group):
	if 'Aviation' in artefact_group:
		return 'aviation'
	elif 'Vacuum Tubes' in artefact_group:
		return 'vacuum'
	elif 'Railway Transportation'in artefact_group:
		return 'railway'
	else:
		return 'other_group'
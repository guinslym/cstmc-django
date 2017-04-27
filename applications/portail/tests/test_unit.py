import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from applications.portail.models import Artefact
pytestmark = pytest.mark.django_db
from django.template import Context, Template
from applications.portail.templatetags.portail_extras import (
get_image,
get_objname,
get_most_common_objname,
get_materials,
get_country,
get_categories,
get_groups,
)
from applications.portail.utils import (
get_background_image,
language_set,
	)

class TestUnit(TestCase):

    def test_background_image(self):
        image = [
                'camera-1149767_1280.jpg',
                'camera-711025_1280.jpg',
                'clock-tower-190677_1280.jpg',
                'car-2072471_1280.jpg',
            ]
        result = get_background_image()
        result = result.split('/')[1]
        assert result in image

    @pytest.mark.skip(reason="function not implemented")
    def test_language_set(self):
    	result = language_set()
    	assert result in ['FR', 'EN']

    @pytest.mark.skip(reason="function not implemented")
    def test_language_set(self):
    	result = language_set()
    	assert result.isupper()

    def test_template_tag_get_image(self):
        result = get_image()
        assert 'Image' in result

    @pytest.mark.skip(reason="function not implemented")
    def test_template_tag_get_objname(self):
        obj = mixer.cycle(60).blend('portail.Artefact', ObjectName=mixer.sequence('objname{0}'))
        result = get_objname()
        assert len(result) == 20
        
    @pytest.mark.skip(reason="function not implemented")
    def test_template_tag_get_most_common_objname(self):
        obj = mixer.cycle(60).blend('portail.Artefact', ObjectName=mixer.sequence('objname{0}'))
        result = get_most_common_objname()
        assert len(result) == 20

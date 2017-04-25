
import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestArtefact:
    def test_init(self):
        obj = mixer.blend('portail.Artefact')
        assert obj.pk == 1, 'Should save an instance'

    def test_null_field(self):
    	obj = mixer.blend('portail.Artefact')
    	assert isinstance(obj.IDNO, None.__class__)

    def test_URLField_field(self):
    	obj = mixer.blend('portail.Artefact', URLField="http://www.url.com")
    	assert "www" in obj.URLField
    	assert "." in obj.URLField
    	assert "http" in obj.URLField
    	assert len((obj.URLField).split('.') ) > 1

    def test_null_field_with_content(self):
    	obj = mixer.blend('portail.Artefact', IDNO='hello')
    	assert isinstance(obj.IDNO, str)
    
    def test_relationship(self):
    	obj = mixer.blend('portail.Description')
    	assert obj.artefact.id == 1
    	art = mixer.blend('portail.Artefact')
    	obj = mixer.blend('portail.Description', artefact=art)
    	assert obj.artefact.id == 2

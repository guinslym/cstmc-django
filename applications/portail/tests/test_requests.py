import pytest
import platform
from django.core import mail
from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.test import RequestFactory
from mock import patch
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from django.test import TestCase
from django.test.client import RequestFactory
from applications.portail.views import (
ArtefactHomeView,
ArtefactSearchView,
ArtefactDetailView,
ArtefactSearchView,
    )
from django.core.urlresolvers import reverse
from django.test import  Client
from django.core.urlresolvers import reverse_lazy
from mixer.backend.django import mixer
from applications.portail.models import Artefact


class RequestTests(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        # Add records to test DB

    def test_home_view(self):
        request = self.factory.get('/')
        response = ArtefactHomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_search_view(self):
        request = self.factory.get('/search', {'searchKey':'hammer'})
        response = ArtefactSearchView.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    @pytest.mark.xfail
    def test_detail_view(self):
        '''
        I need to find out how to make this View work within the Test list
        '''
        obj = mixer.cycle(5).blend('portail.Artefact', ObjectName=mixer.sequence('objname{0}'))
        artefact = Artefact.objects.first()
        response = self.factory.get(reverse('artefact_detail', args=[artefact.id]))
        #request = self.factory.get('/', {'pk':10})
        #response = ArtefactDetailView.as_view()(request, pk=10)
        self.assertEqual(response.status_code, 200)

    @pytest.mark.skip(reason="function not implemented")
    def test_advanced_search_view(self):
        assert True


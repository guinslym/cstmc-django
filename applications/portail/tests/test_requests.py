import pytest
from django.core import mail
from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.test import RequestFactory
from mock import patch
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from django.test import TestCase
from django.test.client import RequestFactory
from applications.portail.views import ArtefactListView, ArtefactSearchView


class RequestTests(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        # Add records to test DB

    def test_home_view_without_client(self):
        request = self.factory.get('/')
        response = ArtefactListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Canad")


class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = ArtefactListView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'

    def test_search(self):
        post = mixer.blend('portail.Artefact')
        data = {'searchKey': 'tube'}
        req = RequestFactory().get('/portail/search/', data=data)
        req._dont_enforce_csrf_checks = True
        pytest.set_trace()
    
    def test_post(self):
        post = mixer.blend('portail.Artefact')
        data = {'body': 'New Body Text!'}
        req = RequestFactory().post('/', data=data)
        req.user = AnonymousUser()

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
    )
from django.core.urlresolvers import reverse
from django.test import  Client
from django.core.urlresolvers import reverse_lazy


class RequestTests(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        # Add records to test DB

    def test_home_view_without_client(self):
        request = self.factory.get('/')
        response = ArtefactHomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_search_view(self):
        pass
        
    def test_detail_view(self):
        pass


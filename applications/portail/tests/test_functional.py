import platform
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.common.keys import Keys
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils import formats
from selenium import webdriver
import pytest

@pytest.mark.skip(
    platform.system() == 'Windows', 
    reason="couldn't run Selenium in my Windows machine :(")
class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.WebDriver()
        self.selenium.implicitly_wait(3)

    def tearDown(self):
        self.selenium.quit()

    # Auxiliary function to add view subdir to URL
    def _get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.selenium.get(self._get_full_url("portail:artefact_home"))
        self.assertIn(u'Science and Technology', self.selenium.title)

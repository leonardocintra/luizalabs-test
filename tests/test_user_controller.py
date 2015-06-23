import http
import urllib
from unittest import TestCase
from app import settings


class UserControllerTest(TestCase):

    def setUp(self):
        self.fb_id = 'coder42'

    def test_list(self):
        conn = http.client.HTTPSConnection("graph.facebook.com/")
        params = urllib.parse.urlencode(settings.FACEBOOK_GRAPH)

        conn.request("GET", self.fb_id, params)
        resp = conn.getresponse()
        return resp

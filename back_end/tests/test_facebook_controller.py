import requests
from unittest import TestCase


class FacebookControllerTest(TestCase):

    def setUp(self):
        self.url = 'http://localhost:8080/api/facebook/{}'

    def test_detail(self):
        """ GET /api/facebook/<pk> must be return status code 200. """
        fb_id = 4
        resp = requests.get(self.url.format(fb_id))
        self.assertEqual(200, resp.status_code)

    def test_fb_id_is_none(self):
        """ GET /api/facebook/<pk> must be return status code 404.
        """
        fb_id = ''
        resp = requests.get(self.url.format(fb_id))
        self.assertEqual(404, resp.status_code)

    def test_fb_id_invalid(self):
        """ GET /api/facebook/<pk> must be return status code 404. """
        fb_id = 3218090948914
        resp = requests.get(self.url.format(fb_id))
        self.assertEqual(404, resp.status_code)

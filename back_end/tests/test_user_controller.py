import requests
from unittest import TestCase
from app.models import db
from app.models.user import User


class UserControllerTest(TestCase):

    def setUp(self):
        self.fb_id = 'coder42'
        self.base_url = "http://127.0.0.1:8080/api{}"
        self.fb_id = {'fb_id': '546506545'}
        self.data = {'fb_id': '321312432432',
                     'username': 'Tereza.Bulkow.41',
                     'name': 'Tereza Bulkow',
                     'gender': 'female',
                     'birthday': '1978-10-07'}
        self.user = User.query.first()

    def test_list(self):
        """ GET /api/users must be return status code 200. """
        resp = requests.get(self.base_url.format("/users"))
        self.assertEqual(200, resp.status_code)

    def test_list_paginate(self):
        """ GET /api/users?page=<page> must be return status code 200. """
        resp = requests.get(self.base_url.format("/users?page=2"))
        self.assertEqual(200, resp.status_code)

    def test_list_search(self):
        """ GET /api/users?search=<word> must be return status code 200. """
        resp = requests.get(self.base_url.format("/users?search=Tereza Bulkow"))
        self.assertEqual(200, resp.status_code)

    def test_detail(self):
        """ GET /api/users/<pk> must be return status code 200. """
        url = self.base_url.format("/users/{}".format(self.user.id))
        resp = requests.get(url)
        self.assertEqual(200, resp.status_code)

    def test_post(self):
        """ POST /api/users/ must be return status code 201 <Created>. """
        url = self.base_url.format("/users/")
        resp = requests.post(url, self.data)
        self.assertEqual(201, resp.status_code)

    def test_post_required_facebook_id(self):
        """ POST /api/user must be return status code 428 <Precondition Required>.
        """
        url = self.base_url.format("/users/")
        resp = requests.post(url, {'fb_id': None})
        self.assertEqual(400, resp.status_code)

    def test_put(self):
        """ PUT /api/users/<pk> must be return status code 200. """
        url = self.base_url.format("/users/{}".format(self.user.id))
        resp = requests.put(url, self.data)
        self.assertEqual(200, resp.status_code)

    def test_delete(self):
        """ DELETE /api/users/<pk> must be return status code 204 <No Content>.
        """
        user = User.query.order_by(db.desc(User.fb_id)).first()
        url = self.base_url.format("/users/{}".format(user.id))
        resp = requests.delete(url)
        self.assertEqual(204, resp.status_code)

    def test_post_in_get(self):
        """ POST /api/users must be return status code 405 <Method Not Allowed>.
        """
        url = self.base_url.format("/users")
        resp = requests.post(url)
        self.assertEqual(405, resp.status_code)

    def tearDownClass(cls):
        User.query.delete()

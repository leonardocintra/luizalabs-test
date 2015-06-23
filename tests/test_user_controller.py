import requests
from unittest import TestCase
from app.models.user import User
from app import settings


class UserControllerTest(TestCase):

    def setUp(self):
        self.fb_id = 'coder42'
        self.base_url = "http://127.0.0.1:8080/api{}"
        self.data = {'fb_id': 546506545,
                     'username': 'theus.oliveira',
                     'name': 'Matheus Oliveira',
                     'gender': 'male',
                     'birthday': '07/10/1988'}
        self.user = User(fb_id=231321321,
                         username='theus.holiveira',
                         name='Matheus Oliveira').save()

    def test_list(self):
        """ GET /users must be return status code 200. """
        resp = requests.get(self.base_url.format("/users"))
        self.assertEqual(200, resp.status_code)

    def test_detail(self):
        """ GET /user/<pk> must be return status code 200. """
        resp = requests.get(
            self.base_url.format("/user/{}".format(self.user.id)))
        self.assertEqual(200, resp.status_code)

    def test_post(self):
        """ POST /user must be return status code 201. """
        resp = requests.post(self.base_url.format("/user"), data=self.data)
        self.assertEqual(201, resp.status_code)

    def test_put(self):
        """ PUT /user/<pk> must be return status code 200. """
        resp = requests.put(
            self.base_url.format("/user/{}".format(self.user.id)),
            data=self.data)
        self.assertEqual(200, resp.status_code)

    def test_delete(self):
        """ DELETE /user/<pk> must be return status code 204. """
        print(self.base_url.format("/user/1"))
        resp = requests.delete(
            self.base_url.format("/user/{}".format(self.user.id)))
        self.assertEqual(204, resp.status_code)

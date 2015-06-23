from unittest import TestCase
from app.models import Session
from app.models.user import User


class UserTest(TestCase):

    def setUp(self):
        self.user = User(fb_id=231321321,
                         username='theus.holiveira',
                         name='Matheus Oliveira')

    def test_save(self):
        """ User save """
        self.assertTrue(self.user.save())

    def tearDown(self):
        Session.rollback()

import http
import urllib
from beer.controllers import BeerAPIView
from app import settings
from app.models.user import User


class UserView(BeerAPIView):

    def list(self):
        return '[{}]'

    def detail(self, pk):
        return '{id: 1, fb_id: 802093201}'

    def create(self):
        return "Create:"

    def update(self, pk):
        return "Update: {}".format(pk)

    def delete(self, pk):
        user = User.get(pk=pk).delete()
        return "Delete: {}".format(user)

    def __get_facebook_user(self, fb_id):
        conn = http.client.HTTPSConnection("graph.facebook.com/")
        params = urllib.parse.urlencode(settings.FACEBOOK_GRAPH)

        conn.request("GET", fb_id, params)
        resp = conn.getresponse()
        return resp

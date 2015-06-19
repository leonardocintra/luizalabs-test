from bottle import request
from app.models.user import User
import http


class UserView:

    def index(self):
        return "List"

    def detail(self, pk):
        return "Detail: {}".format(pk)

    def create(self):
        fb_id = request.POST.get("fb_id")
        return "Create: {}".format(fb_id)

    def update(self, pk):
        return "Update: {}".format(pk)

    def delete(self, pk):
        return "Delete: {}".format(pk)

    def __get_facebook_user(self, fb_id):
        conn = http.client.HTTPConnection("graph.facebook.com/")
        conn.request("GET", fb_id)
        resp = conn.getresponse()
        return resp

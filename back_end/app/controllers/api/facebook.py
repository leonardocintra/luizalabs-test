from bottle import response
from app.helpers.facebook import FacebookAPI


class FacebookController:

    def detail(self, pk):
        user = FacebookAPI(pk).user()
        if user is None:
            response.status = 404
            return ""
        return user

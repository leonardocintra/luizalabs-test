import requests
from bottle import response
from app import settings


class FacebookController:

    def auth(self):
        url = "https://www.facebook.com/dialog/oauth"
        params = {
            'client_id': settings.FACEBOOK_GRAPH['app_id'],
            'redirect_uri': 'http://127.0.0.1:3000/'
        }
        resp = requests.get(url, params=params)
        return resp.content

    def detail(self, pk):
        if not pk:
            response.status = 428
            return ""

        url = "https://graph.facebook.com/v2.3/{}".format(pk)
        resp = requests.get(url, params=settings.FACEBOOK_GRAPH)
        data = resp.json()
        error = data.get('error')
        if error:
            if error['code'] == 190:
                response.status = 400
                return 'Token expirado.'
            response.status = 404
            return ""
        return data

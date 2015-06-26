import http.client
import urllib.parse
import json
from app import settings


class FacebookAPI:

    def __init__(self, fb_id):
        conn = http.client.HTTPSConnection("graph.facebook.com")
        params = urllib.parse.urlencode(settings.FACEBOOK_GRAPH)
        uri = "/v2.3/{}?{}".format(fb_id, params)
        conn.request("GET", uri)
        self.resp = conn.getresponse()

    def user(self):
        resp = self.resp.read().decode('utf-8')
        resp = json.loads(resp)
        error = resp.get('error')

        if error is not None:
            return None
        return resp

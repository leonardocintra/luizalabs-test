import http
import json
from bottle import Bottle, request

facebook_app = Bottle()


@facebook_app.get('/api/facebook/')
def list():
    return 'List'


@facebook_app.get('/api/facebook/<facebook_id>/')
def get(facebook_id):
    user = __get_facebook_user(facebook_id)
    return user     # template('home/index.html')


@facebook_app.post('/api/facebook/')
def post():
    facebook_id = request.post.get('facebook_id')
    user = __get_facebook_user(facebook_id)
    return user     # template('home/index.html')


@facebook_app.delete('/api/facebook/<facebook_id>/')
def delete(facebook_id):
    return "Delete"


def __get_facebook_user(facebook_id):
    conn = http.client.HTTPConnection("graph.facebook.com")
    conn.request("GET", "/coder42")

    resp = conn.getresponse()
    data = resp.read()

    return json.loads(data.decode("utf-8"))

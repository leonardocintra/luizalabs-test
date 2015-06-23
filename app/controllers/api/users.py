import http
import urllib
import json
from bottle import Bottle, request
from app import settings
from app.models.user import User


user_api = Bottle()


@user_api.get('/')
def list():
    pager = 20
    query = User.query.all()
    paginator = len(query) // pager
    print(len(query))
    return {
        'page': 1,
        'paginator': paginator,
        'objects': json.dumps([obj.as_json() for obj in query])
    }


@user_api.get('/<pk>')
def detail(pk):
    return '%s {id: 1, fb_id: 802093201}' % pk


@user_api.post('/')
def create():
    data = request.POST
    return "Create: {}".format(data)


@user_api.put('/<pk>')
def update(pk):
    return "Update: {}".format(pk)


@user_api.delete('/<pk>')
def delete(pk):
    return "Delete: {}".format(pk)


def __get_facebook_user(fb_id):
    conn = http.client.HTTPSConnection("graph.facebook.com/")
    params = urllib.parse.urlencode(settings.FACEBOOK_GRAPH)

    conn.request("GET", fb_id, params)
    resp = conn.getresponse()
    return resp

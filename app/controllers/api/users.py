import json
import requests
from bottle import Bottle, request, HTTPResponse
from app import settings
from app.models.user import User


user_api = Bottle()


@user_api.get('/users')
def list():
    pager = 20
    page = request.GET.get('page', 1)
    query = User.query.all()
    paginator = len(query) // pager

    context = []
    if query:
        context = {
            'page': page,
            'paginator': paginator,
            'objects': json.dumps([obj.as_json() for obj in query])
        }
    return HTTPResponse(context, status=200)


@user_api.get('/user/<pk>')
def detail(pk):
    user = User.query.get(pk)
    return HTTPResponse(user.as_json(), status=200)


@user_api.post('/user')
def create():
    fb_user = __get_facebook_user(request.POST.get('fb_id'))

    user = User(fb_id=fb_user.get('id'),
                username=fb_user.get('username'),
                name=fb_user.get('name'))
    if user.is_valid():
        user.save()
        return HTTPResponse(user.as_json(), status=201)
    return HTTPResponse(user.errors_json(), status=400)


@user_api.put('/user/<pk>')
def update(pk):
    return "Update: {}".format(pk)


@user_api.delete('/user/<pk>')
def delete(pk):
    user = User.query.get(pk)
    user = user.delete()
    return HTTPResponse(status=204)


def __get_facebook_user(fb_id):
    url = "https://graph.facebook.com/v2.3/{}".format(fb_id)
    resp = requests.get(url, params=settings.FACEBOOK_GRAPH)
    data = resp.json()
    print(data)
    if not data.get('error') is None:
        raise HTTPResponse(
            json.dumps({'error': 'Usuário inválido ou não encontrado.'}),
            status=404)
    return data

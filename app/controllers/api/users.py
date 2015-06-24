import json
import requests
from bottle import Bottle, request, HTTPResponse, HTTPError
from app import settings
from app.models import Pagination, serialize
from app.models.user import User


user_api = Bottle()


@user_api.get('/users')
def list():
    page = request.GET.get('page', 1)
    per_page = 40
    query = User.query
    pagination = Pagination(query, page, per_page)

    return HTTPResponse({
        'pages': pagination.pages,
        'prev': pagination.prev,
        'next': pagination.next,
        'objects': serialize(pagination.objects)},
        status=200)


@user_api.get('/user/<pk>')
def detail(pk):
    try:
        return User.get_or_404(id=pk).as_json()
    except HTTPError:
        return HTTPResponse('Objeto não encontrado.', status=404)


@user_api.post('/user')
def create():
    fb_id = request.POST.get('fb_id')
    if fb_id is None:
        return HTTPResponse('Informe o ID de usuário do Facebook', status=428)

    data = __get_facebook_user(fb_id)
    # data = request.params
    user = User(fb_id=data.get('id'),
                username=data.get('username', ''),
                name=data.get('name', ''),
                gender=data.get('gender', ''),
                birthday=data.get('birthday', None))

    if user.is_valid():
        user.save()
        return HTTPResponse(user.as_json(), status=201)
    return HTTPResponse(user.errors_json(), status=400)


@user_api.put('/user/<pk>')
def update(pk):
    data = request.params

    user = User.get_or_404(id=pk)
    user.username = data.get('username', '')
    user.name = data.get('name', '')
    user.gender = data.get('gender', '')
    user.birthday = data.get('birthday', '')

    if user.is_valid():
        user.save()
        return HTTPResponse(user.as_json(), status=200)

    return HTTPResponse(user.errors_json(), status=400)


@user_api.delete('/user/<pk>')
def delete(pk):
    user = User.query.get(pk)
    user = user.delete()
    return HTTPResponse(status=204)


def __get_facebook_user(fb_id):
    url = "https://graph.facebook.com/v2.3/{}".format(fb_id)
    resp = requests.get(url, params=settings.FACEBOOK_GRAPH)
    data = resp.json()

    error = data.get('error')
    if error:
        msg = 'Usuário inválido ou não encontrado.'
        if error['code'] == 190:
            msg = 'Seu token expirou. Solicite outro em: https://developers.facebook.com/'
        raise HTTPResponse(json.dumps({'error': msg}), status=404)
    return data

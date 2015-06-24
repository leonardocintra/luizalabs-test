import json
import requests
from bottle import Bottle, HTTPResponse
from app import settings


fb_api = Bottle()


@fb_api.get('/<pk>')
def detail(fb_id):
    if not fb_id:
        return HTTPResponse('Informe o ID de usuário do Facebook', status=428)

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

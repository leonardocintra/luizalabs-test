import json
import requests
from bottle import response
from app import settings


class FacebookController:

    def detail(self, fb_id):
        if not fb_id:
            response.status = 428
            return 'Informe o ID de usuário do Facebook'

        url = "https://graph.facebook.com/v2.3/{}".format(fb_id)
        resp = requests.get(url, params=settings.FACEBOOK_GRAPH)
        data = resp.json()

        error = data.get('error')
        if error:
            msg = 'Usuário inválido ou não encontrado.'
            if error['code'] == 190:
                msg = 'Seu token expirou. Solicite outro em: https://developers.facebook.com/'
                response.status = 404
            raise {'error': msg}
        return data

import requests
from bottle import request, response, HTTPError
from app import settings
from app.models import Pagination, serialize
from app.models.user import User


class UserController:

    def list(self):
        page = request.GET.get('page', 1)
        per_page = 5
        query = User.query
        pagination = Pagination(query, page, per_page)

        context = {
            'pages': pagination.pages,
            'prev': pagination.prev,
            'next': pagination.next,
            'current': page,
            'objects': serialize(pagination.objects)
        }
        return context

    def detail(self, pk):
        user = User.get_or_404(id=pk)
        if user:
            return user.as_json()

    def create(self):
        fb_id = request.POST.get('fb_id')
        if fb_id is None:
            response.status = 428
            return {'msg': 'Informe um ID de usuário do Facebook'}

        data = self.__get_facebook_user(fb_id)
        # data = request.params
        user = User(fb_id=data.get('id'),
                    username=data.get('username', ''),
                    name=data.get('name', ''),
                    gender=data.get('gender', ''),
                    birthday=data.get('birthday', None))

        if user.is_valid():
            user.save()
            response.status = 201
            return user.as_json()
        response.status = 400
        return user.errors_json()

    def update(self, pk):
        data = request.params

        user = User.get_or_404(id=pk)
        user.username = data.get('username', '')
        user.name = data.get('name', '')
        user.gender = data.get('gender', '')
        user.birthday = data.get('birthday', '')

        if user.is_valid():
            user.save()
            return user.as_json()

        response.status = 400
        return user.errors_json()

    def delete(self, pk):
        user = User.query.get(pk)
        user = user.delete()
        response.status = 204
        return""

    def __get_facebook_user(self, fb_id):
        url = "https://graph.facebook.com/v2.3/{}".format(fb_id)
        resp = requests.get(url, params=settings.FACEBOOK_GRAPH)
        data = resp.json()

        error = data.get('error')
        if error:
            msg = 'Usuário inválido ou não encontrado.'
            if error['code'] == 190:
                msg = 'Seu token expirou. Solicite outro em: https://developers.facebook.com/'
            response.status = 400
            return {'msg': msg}
        return data

from bottle import request, response
from app.models import Pagination, serialize
from app.models.user import User


class UserController:

    def list(self):
        page = request.GET.get('page', 1)
        search = request.GET.get('search')
        per_page = 20
        query = User.query

        if search is not None:
            search = '%{}%'.format(search)
            query = User.query.filter(
                User.username.ilike(search) |
                User.fb_id.ilike(search) |
                User.name.ilike(search) |
                User.gender.ilike(search))
        query = query.order_by(User.name)
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
        data = request.params
        user = User(fb_id=data.get('fb_id'),
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
        data = request.forms
        print(request.params.get('username'))

        user = User.get_or_404(id=pk)
        user.username = data.get('username', '')
        user.name = data.get('name', '')
        user.gender = data.get('gender', '')
        user.birthday = data.get('birthday') if data.get('birthday') else None

        print(data.get("username"))

        if user.is_valid():
            user.save()
            return user.as_json()

        print(user.errors_json())
        response.status = 400
        return user.errors_json()

    def delete(self, pk):
        user = User.get_or_404(id=pk)
        user.delete()
        response.status = 204
        return ""

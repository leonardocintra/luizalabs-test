from .controllers import home
from .controllers.api import users

home = home.HomeView()
user = users.UserView()


def urlpatterns(app):
    app.route('/', 'GET', home.index)

    app.route('/api/users/', 'GET', user.index)
    app.route('/api/users/<pk>/', 'GET', user.detail)
    app.route('/api/users/', 'POST', user.create)
    app.route('/api/users/<pk>/', 'PUT', user.update)
    app.route('/api/users/<pk>/', 'DELETE', user.delete)

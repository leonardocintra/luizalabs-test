from .controllers.home import HomeController
from .controllers.api.users import UserController
from .controllers.api.facebook import FacebookController


home = HomeController()
user = UserController()
facebook = FacebookController()


def urlpatterns(app):
    # root route
    app.route('/', 'GET', home.index)

    # Users API routes
    app.route('/api/users/', 'GET', user.list)
    app.route('/api/users/', 'POST', user.create)
    app.route('/api/users/<pk>', 'GET', user.detail)
    app.route('/api/users/<pk>', ['OPTIONS', 'DELETE'], user.delete)
    app.route('/api/users/<pk>', ['OPTIONS', 'PUT'], user.update)

    # Facebook API
    # app.route('/api/facebook/auth/', 'GET', facebook.auth)
    app.route('/api/facebook/<pk>', 'GET', facebook.detail)

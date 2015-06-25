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
    app.route('/api/user/<pk>', 'GET', user.detail)
    app.route('/api/user/', 'POST', user.create)
    app.route('/api/user/<pk>', ['OPTIONS', 'PUT'], user.update)
    app.route('/api/user/<pk>', ['OPTIONS', 'DELETE'], user.delete)

    # Facebook API
    # app.route('/api/facebook/auth/', 'GET', facebook.auth)
    app.route('/api/facebook/<pk>', 'GET', facebook.detail)

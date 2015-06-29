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
    app.route('/api/users', 'GET', user.list)
    app.route('/api/user/', 'POST', user.create)
    app.route('/api/user/<pk>', 'GET', user.detail)
    app.route('/api/user/<pk>', ['OPTIONS', 'DELETE'], user.delete)
    app.route('/api/user/<pk>', ['OPTIONS', 'PUT'], user.update)

    # Facebook API
    app.route('/api/facebook/<pk>', 'GET', facebook.detail)

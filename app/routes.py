from .controllers.home import home_app
from .controllers.api.users import user_api


def routes(app):
    app.merge(home_app)
    app.mount('/api/', user_api)

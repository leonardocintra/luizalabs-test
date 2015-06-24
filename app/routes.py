from .controllers.home import home_app
from .controllers.api.users import user_api
from .controllers.api.facebook import fb_api


def routes(app):
    # root route
    app.merge(home_app)
    # API users routes
    app.mount('/api/', user_api)
    app.mount('/api/', fb_api)

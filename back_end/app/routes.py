from bottle import Bottle
from .controllers.home import home_app
from .controllers.api.users import user_api
from .controllers.api.facebook import fb_api

Routes = Bottle()


# root route
Routes.merge(home_app)
# API users routes
Routes.mount('/api/', user_api)
Routes.mount('/api/facebook/', fb_api)

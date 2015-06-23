from . import Bottle
from .controllers.home import home_app
from .controllers.api.users import user_api

Routes = Bottle()

Routes.merge(home_app),
Routes.mount('/api/users/', user_api)

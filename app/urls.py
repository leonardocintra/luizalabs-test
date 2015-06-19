from bottle import Bottle
from .controllers import home
from .controllers.api import facebook

urls = Bottle()

urls.merge(home.home_app)
urls.merge(facebook.facebook_app)

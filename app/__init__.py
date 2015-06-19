import bottle
import logging.config
from app import urls


class Beer:

    def __init__(self,
                 server='auto',
                 host='0.0.0.0',
                 port=3000,
                 debug=False,
                 reloader=True,
                 template_path='./app/views/',
                 logging_config=None):
        self.server = server
        self.host = host
        self.port = port
        self.debug = debug
        self.reloader = reloader
        self.template_path = template_path

        self.app = bottle.Bottle()

        urls.urlpatterns(self.app)

        if template_path not in bottle.TEMPLATE_PATH:
            bottle.TEMPLATE_PATH.append(template_path)

        bottle.debug(self.debug)
        if logging_config is not None:
            logging.config.dictConfig(logging_config)


class BeerView:

    def __init__(self):
        self.request = bottle.request

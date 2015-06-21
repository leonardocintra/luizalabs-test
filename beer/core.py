import bottle
import logging.config
from bottle.ext import sqlalchemy
from .db import Base, Engine
from app import urls


class Beer:

    def __init__(self,
                 server='auto',
                 host='0.0.0.0',
                 port=5000,
                 debug=False,
                 reloader=True,
                 template_path='./app/views/',
                 logging_config=None,
                 echo_db=True):
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

        sqlalchemy_plugin = sqlalchemy.Plugin(
            Engine,
            Base.metadata,
            keyword='db',
            create=True,
            commit=True,
            use_kwargs=False)

        self.plugin_install(sqlalchemy_plugin)

    def plugin_install(self, plugin):
        self.app.install(plugin)

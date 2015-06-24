from __future__ import unicode_literals
import os
import click
import env
from bottle import Bottle, run, response, HTTPResponse, static_file, TEMPLATE_PATH
from bottle.ext import sqlalchemy
from app.models import engine, Model
from app.routes import urlpatterns
from app import settings


TEMPLATE_PATH.insert(0, settings.TEMPLATE_PATH)


app = Bottle()

urlpatterns(app)


@app.hook('after_request')
def enable_cors():
    hosts = '*' if settings.DEBUG else settings.ALLOWED_HOSTS
    response.headers['Access-Control-Allow-Origin'] = hosts


@app.route('/assets/<path:path>', name='assets')
def assets(path):
    yield static_file(path, root=settings.STATIC_PATH)

sqlalchemy_plugin = sqlalchemy.Plugin(
    engine,
    Model.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False
)

# Register bottle plugins
app.install(sqlalchemy_plugin)


@click.group()
def cmds():
    pass


@cmds.command()
@click.option('--port', default=os.environ.get('PORT', 8080), type=int,
              help=u'Set application server port!')
@click.option('--ip', default='0.0.0.0', type=str,
              help=u'Set application server ip!')
@click.option('--debug', default=False,
              help=u'Set application server debug!')
def runserver(port, ip, debug):
    run(app, host=ip, port=port,
        debug=settings.DEBUG, reloader=settings.DEBUG)
    click.echo('Start server at: {}:{}'.format(ip, port))
    run(app=app, host=ip, port=port, debug=debug, reloader=debug)


@cmds.command()
def test():
    import unittest
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    testRunner = unittest.runner.TextTestRunner()
    testRunner.run(tests)


if __name__ == '__main__':
    cmds()
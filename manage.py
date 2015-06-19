from bottle import Bottle, run, static_file, TEMPLATE_PATH
from app import settings
from app.urls import urls


app = Bottle()

TEMPLATE_PATH.insert(0, settings.TEMPLATE_PATH)

# Register app urls
app.merge(urls)


@app.route('{}/<path:path>'.format(settings.STATIC_URL), name='assets')
def assets(path):
    yield static_file(path, root=settings.STATIC_ROOT)


def runserver(port='5000', ip='0.0.0.0', debug=True):
    run(app=app, host=ip, port=port, debug=debug, reloader=debug)

if __name__ == '__main__':
    runserver()

from bottle import Bottle, template

home_app = Bottle()


@home_app.get('/')
def index():
    return template('home/index.html')

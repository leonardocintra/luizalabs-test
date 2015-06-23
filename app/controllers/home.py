from bottle import Bottle


home_app = Bottle()


@home_app.route('/')
def index():
    return ""

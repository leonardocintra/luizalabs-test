from bottle import Bottle, template


home_app = Bottle()


@home_app.route('/')
def index():
    return template("index.html")

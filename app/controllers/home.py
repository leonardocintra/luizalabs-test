from bottle import template


class HomeView:

    def index(self):
        return template('index.html')

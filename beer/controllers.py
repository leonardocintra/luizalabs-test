import bottle
from bottle import jinja2_template as template


class BeerView:

    def __init__(self):
        self.request = bottle.request

    def render(self, template_name, **kwargs):
        return template(template_name, **kwargs)


class BeerAPIView(BeerView):
    pass

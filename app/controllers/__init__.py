class MethodView:
    _methods = ['index', 'show', 'new', 'create', 'edit', 'update', 'delete']
    http_verbs = ['GET', 'POST', 'PUT', 'DELETE']

    @classmethod
    def as_view(cls, app):
        cls.__register(app)

    @classmethod
    def __register(cls, app):
        prefix = cls.prefixed(cls.__name__)

        app.route(prefix, 'GET', cls.index)

    @classmethod
    def prefixed(cls, prefix):
        return '/' if prefix.lower() == 'home' else prefix

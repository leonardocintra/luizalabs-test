import json
import sqlalchemy as db
from bottle import abort
from sqlalchemy.ext.declarative import declarative_base
from math import ceil
from datetime import date
from app import settings


# SQL Alchemy config
connection_string = "{ENGINE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}".format(
    **settings.DATABASE)
engine = db.create_engine(connection_string)
Session = db.orm.scoped_session(db.orm.sessionmaker(bind=engine))


class Pagination:

    def __init__(self, query, page, per_page):
        self.query = query
        self.page = int(page)
        self.per_page = per_page
        self.total = query.count()

    @property
    def pages(self):
        if self.per_page == 0:
            pages = 0
        else:
            pages = int(ceil(self.total / self.per_page))
        return pages

    @property
    def objects(self):
        offset = (self.page - 1) * self.per_page
        return self.query.limit(self.per_page).offset(offset).all()

    @property
    def prev(self):
        return self.page - 1 if self.page >= 1 else self.page

    @property
    def next(self):
        return self.page + 1 if self.page < self.pages else None


class _ModelValidationMixin:

    """ Model Validation fields """

    def attr_validate(self, col, field, required=True, min_length=None):
        msgs = {}

        if required and not field:
            msgs.update(required=self.__error_msgs('required'))

        if field and min_length is not None and len(field) < min_length:
            msgs.update(
                length=self.__error_msgs('length'), min_length=min_length)

        return {self.__table__.columns[col].name: msgs} if len(msgs) else False

    def validates(self, *args):
        self.errors = []
        for arg in args:
            if arg:
                self.errors.append(arg)
        return False if len(self.errors) else True

    def errors_json(self):
        return json.dumps({'error': self.errors})

    def __error_msgs(self, msg, **kwargs):
        error_msg = {
            'required': 'Campo obrigatório.',
            'integer': "Informe um número válido.",
            'str': None,
            'length': "Campo deve conter {} ou mais caracteres.".format(
                kwargs.get('min_length', '')),
        }
        return error_msg[msg]


class _BaseQueryMixin:

    """ Base Query Mixin
        Provide a additionals method to query
    """
    query = Session.query_property()

    @classmethod
    def get_or_404(cls, format=None, **kwargs):
        query = cls.query.filter_by(**kwargs).first()
        if query is None:
            abort(404)
        return query

    @classmethod
    def list_or_404(cls, format=None, **kwargs):
        query = cls.query.filter_by(**kwargs)
        if query is None:
            abort(404)
        return query

    def save(self):
        try:
            if self.id is None:
                Session.add(self)
            Session.commit()
        except db.exc.IntegrityError:
            Session.close()
            raise abort(409)
        return self

    def delete(self):
        session = Session
        session.delete(self)
        session.commit()
        session.close()


class _BaseModel(_BaseQueryMixin, _ModelValidationMixin):

    """ Helper Base Model
    """

    def as_json(self):
        data = {}
        for c in self.__table__.columns:
            attr = getattr(self, c.name)
            val = str(attr) if type(attr) is date else attr
            data[c.name] = val
        return data

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self)

# Base Model
Model = declarative_base(cls=_BaseModel)


def serialize(query):
    serialized = []
    if query:
        serialized = [obj.as_json() for obj in query]
    return serialized

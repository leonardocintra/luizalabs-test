import json
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from app import settings


# SQL Alchemy config
connection_string = "{ENGINE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}".format(
    **settings.DATABASE)
engine = db.create_engine(connection_string)
Session = db.orm.scoped_session(db.orm.sessionmaker(bind=engine))


class ModelValidationMixin:
    """ Model Validation fields """

    def attr_validate(self, col, field, required=True, min_length=None):
        msgs = {}

        if required and not field:
            msgs.update(required=self.__error_msgs('required'))

        if not min_length is None and len(field) < min_length:
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


class _BaseModel(ModelValidationMixin):

    """
        Helper Base Model
    """
    query = Session.query_property()

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self)

    def as_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def save(self):
        try:
            Session.add(self)
            Session.commit()
            return True
        except db.exc.SQLAlchemyError:
            raise

# Base Model
Model = declarative_base(cls=_BaseModel)

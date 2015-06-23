import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from app import settings


# SQL Alchemy config
connection_string = "{ENGINE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}".format(
    **settings.DATABASE)
engine = db.create_engine(connection_string)
Session = db.orm.scoped_session(db.orm.sessionmaker(bind=engine))


class _BaseModel(object):
    """
        Helper Base Model
    """
    query = Session.query_property()

    def save(self):
        try:
            Session.add(self)
            Session.commit()
            return True
        except:
            raise

    def as_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self)


# Base Model
Model = declarative_base(cls=_BaseModel)

from app import settings
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Model = declarative_base()


def parse_db(params):
    return "{engine}:///{user}:{passwd}@{host}:{port}/{name}".format(
        engine=params['ENGINE'],
        user=params['USER'],
        passwd=params['PASSWORD'],
        host=params['HOST'],
        port=params['PORT'],
        name=params['NAME'])


Engine = create_engine(parse_db(settings.DATABASE))
Session = sessionmaker(bind=Engine)

sqlalchemy_plugin = sqlalchemy.Plugin(
    Engine,
    Model.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False)

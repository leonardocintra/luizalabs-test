from beer.conf import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


"""
def connection_string():
    params = settings.DATABASE
    return "{engine}:///{user}:{passwd}@{host}:{port}/{name}".format(
        engine=params['ENGINE'],
        user=params['USER'],
        passwd=params['PASSWORD'],
        host=params['HOST'],
        port=params['PORT'],
        name=params['NAME'])
"""


connection_string = "{ENGINE}:///{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}".format(
    **settings.DATABASE)

Base = declarative_base()
Engine = create_engine(connection_string)
Session = sessionmaker(bind=Engine)

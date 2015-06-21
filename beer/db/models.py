from sqlalchemy import *
from beer.db import Base, Session


class BeerModel:
    __tablename__ = 'logs'

    def __init__(self):
        self.engine = Session

    def all(self):
        return Session(self).all()

    def filter(self, **kwargs):
        return Session(self).filter(**kwargs).all()

    def save(self):
        obj = Session.add(self)
        self.__commit()
        return obj

    def update(self):
        obj = Session.update(self)
        self.__commit()
        return obj

    def delete(self):
        obj = Session.delete(self)
        self.__commit()
        return obj

    def __commit(self):
        return self.Session.commit()

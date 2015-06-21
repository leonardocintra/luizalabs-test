from beer.core import Model, session


class BeerModel(Model):

    def __init__(self):
        self.engine = session

    def all(self):
        return session(self).all()

    def filter(self, **kwargs):
        return session(self).filter(**kwargs).all()

    def save(self):
        obj = session.add(self)
        self.__commit()
        return obj

    def update(self):
        obj = session.update(self)
        self.__commit()
        return obj

    def delete(self):
        obj = session.delete(self)
        self.__commit()
        return obj

    def __commit(self):
        return self.session.commit()

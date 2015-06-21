from beer.db import models


class User(models.Base):
    __tablename__ = 'users'

    id = models.Column(models.Integer, primary_key=True)
    fb_id = models.Column(models.Integer)
    username = models.Column(models.String(50))
    name = models.Column(models.String(80))
    gender = models.Column(models.String(10))
    birthday = models.Column(models.Date)

    def __str__(self):
        return self.name

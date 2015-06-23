from app.models import *


class User(Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, db.Sequence('user_id'), primary_key=True)
    fb_id = db.Column(db.Integer)
    username = db.Column(db.String(50))
    name = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    birthday = db.Column(db.Date)

    def __str__(self):
        return self.name

    def is_valid(self):
        return self.validates(
            self.attr_validate('fb_id', self.fb_id, required=True),
            self.attr_validate('name', self.name, min_length=3)
        )

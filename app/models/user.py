from sqlalchemy import Column, Integer, String, Date


class User:
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fb_id = Column(Integer)
    username = Column(String(50))
    name = Column(String(80))
    gender = Column(String(10))
    birthday = Column(Date)

    def __str__(self):
        return self.name

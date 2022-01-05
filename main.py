# import sqlalchemy
# from sqlalchemy import *
# from sqlalchemy.orm import mapper
# engine = create_engine('sqlite:///:memory:', echo=True)
# metadata = MetaData()
# users_table = Table('users', metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('name', String),
#                     Column('fullname', String),
#                     Column('password', String)
#                     )
# metadata.create_all(engine)
#
#
# class User:
#     def __init__(self, name, fullname, password):
#         self.name = name
#         self.fullname = fullname
#         self.password = password
#
#     def __repr__(self):
#         return f"{self.name, self.fullname, self.password}"
#
#
# mapper(User, users_table)
# user = User("1", "33", "3333")
# print(user.id)
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)


# Создание таблицы
Base.metadata.create_all(engine)
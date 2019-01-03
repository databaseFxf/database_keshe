from orm.Field import *
from orm.orm import *


class User(Model):
    __table__ = "users"
    id = IntegerField(primary_key=True)
    username = StringField(length=10)
    password_hash = StringField(length=10)
    name = StringField(length=10)
    nick_name = StringField(length=10)
    email = StringField(length=14)
    phone = StringField(length=14)
    registration = TimeField()


class UserEvaluation(Model):
    __table__ = "user_evaluation"
    id = IntegerField(primary_key=True)
    username = StringField(length=10)
    movie_id = IntegerField()

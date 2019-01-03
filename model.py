from orm.Field import *
from orm.orm import *


class User(Model):
    __table__ = "users"
    id = IntegerField(primary_key=True)
    username = StringField(length=10)
    password = StringField(length=10)
    name = StringField(length=10)
    nick_name = StringField(length=10)
    email = StringField(length=14)
    phone = StringField(length=14)
    registration_time = TimeField()


class UserEvaluation(Model):
    __table__ = "user_evaluations"
    id = IntegerField(primary_key=True)
    user_id = IntegerField()
    movie_id = IntegerField()
    score = IntegerField()
    status = StringField(length=10)
    evaluation_time = TimeField()




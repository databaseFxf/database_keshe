from orm.Field import *
from orm.orm import Model


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


class UserComment(Model):
    __table__ = "user_comments"
    id = IntegerField(primary_key=True)
    user_id = IntegerField()
    movie_id = IntegerField()
    content = TextField()
    comment_time = TimeField()
    tag = StringField(length=20)


class Celebrate(Model):
    __table__ = "celebrates"
    id = IntegerField(primary_key=True)
    celebrate_name = StringField(20)
    celebrate_sex = StringField(5)
    celebrate_constellation = StringField(20)
    celebrate_birthday = TimeField()
    celebrate_birthplace = StringField(50)
    celebrate_professions = StringField(20)
    celebrate_icon_url = StringField(50)


class CelebrateMovie(Model):
    __table__ = "celebrate_movies"
    id = IntegerField(primary_key=True)
    user_id = IntegerField()
    movie_id = IntegerField()
    role = StringField(length=10)
    this_profession = StringField(length=20)


class Movie(Model):
    __table__ = "movies"
    id = IntegerField(primary_key=True)
    movie_name = StringField(length=30)
    movie_type = StringField(length=20)
    movie_production = StringField(length=20)
    movie_language = StringField(length=20)
    movie_release_date = StringField(length=30)
    movie_length = StringField(length=10)
    movie_aliases = StringField(length=100)
    IMDB_link = StringField(length=50)
    movie_synopsis = TextField()
    movie_poster_url = StringField(50)


class MovieSource(Model):
    __table__ = "movie_sources"
    id = IntegerField(primary_key=True)
    movie_id = IntegerField()
    source_name = StringField(length=20)
    source_url = StringField(length=50)
    source_information = StringField(length=20)

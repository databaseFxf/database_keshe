from models import *
from datetime import datetime


async def create_celebrate_movie(args):
    celebrate_movie = CelebrateMovie()
    for key, value in args.items():
        if hasattr(celebrate_movie, key):
            setattr(celebrate_movie, key, value)
    return await celebrate_movie.save()


async def find_celebrate_movie(id):
    celebrate_movie = await CelebrateMovie.find(id)
    print(celebrate_movie)
    return celebrate_movie


async def find_celebrate_movies():
    celebrate_movies = await CelebrateMovie.findAll()
    for celebrate_movie in celebrate_movies:
        print(celebrate_movie)
    return celebrate_movies


async def delete_celebrate_movie(id):
    celebrate_movie = await CelebrateMovie.find(id)
    return await celebrate_movie.remove()


async def update_celebrate_movie(id, args):
    celebrate_movie = await CelebrateMovie.find(id)
    for key, value in args.items():
        if hasattr(celebrate_movie, key):
            setattr(celebrate_movie, key, value)
    return await celebrate_movie.change()

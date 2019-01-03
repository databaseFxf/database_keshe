from models import *
from datetime import datetime


async def create_movie(args):
    movie = Movie()
    for key, value in args.items():
        if hasattr(movie, key):
            setattr(movie, key, value)
    return await movie.save()


async def find_movie(id):
    movie = await Movie.find(id)
    print(movie)
    return movie


async def find_movies():
    movies = await Movie.findAll()
    for movie in movies:
        print(movie)
    return movies


async def delete_movie(id):
    movie = await Movie.find(id)
    return await movie.remove()


async def update_movie(id, args):
    movie = await Movie.find(id)
    for key, value in args.items():
        if hasattr(movie, key):
            setattr(movie, key, value)
    return await movie.change()

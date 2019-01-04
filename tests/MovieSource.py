from models import *
from datetime import datetime


async def create_movie_source(args):
    movie_source = MovieSource()
    for key, value in args.items():
        if hasattr(movie_source, key):
            setattr(movie_source, key, value)
    return await movie_source.save()


async def find_movie_source(id):
    movie_source = await MovieSource.find(id)
    print(movie_source)
    return movie_source


async def find_movie_sources():
    movie_sources = await MovieSource.findAll()
    for movie_source in movie_sources:
        print(movie_source)
    return movie_sources


async def delete_movie_source(id):
    movie_source = await MovieSource.find(id)
    return await movie_source.remove()


async def update_movie_source(id, args):
    movie_source = await MovieSource.find(id)
    for key, value in args.items():
        if hasattr(movie_source, key):
            setattr(movie_source, key, value)
    return await movie_source.change()

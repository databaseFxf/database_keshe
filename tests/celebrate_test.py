from models import *
from datetime import datetime


async def create_celebrate(args):
    celebrate = Celebrate()
    for key, value in args.items():
        if hasattr(celebrate, key):
            setattr(celebrate, key, value)
    return await celebrate.save()


async def find_celebrate(id):
    celebrate = await Celebrate.find(id)
    print(celebrate)
    return celebrate


async def find_celebrates():
    celebrates = await Celebrate.findAll()
    for celebrate in celebrates:
        print(celebrate)
    return celebrates


async def delete_celebrate(id):
    celebrate = await Celebrate.find(id)
    return await celebrate.remove()


async def update_celebrate(id, args):
    celebrate = await Celebrate.find(id)
    for key, value in args.items():
        if hasattr(celebrate, key):
            setattr(celebrate, key, value)
    return await celebrate.change()

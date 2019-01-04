from models import *
from datetime import datetime


async def create_user(args):
    user = User()
    for key, value in args.items():
        if hasattr(user, key):
            setattr(user, key, value)
    return await user.save()


async def find_user(id):
    user = await User.find(id)
    print(user)
    return user


async def find_users():
    users = await User.findAll()
    for user in users:
        print(user)
    return users


async def delete_user(id):
    user = await User.find(id)
    return await user.remove()


async def update_user(id, args):
    user = await User.find(id)
    for key, value in args.items():
        if hasattr(user, key):
            setattr(user, key, value)
    return await user.change()

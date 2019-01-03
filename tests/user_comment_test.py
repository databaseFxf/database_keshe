from models import *
from datetime import datetime


async def create_user_comment(args):
    user_comment = UserComment()
    for key, value in args.items():
        if hasattr(user_comment, key):
            setattr(user_comment, key, value)
    return await user_comment.save()


async def find_user_comment(id):
    user_comment = await UserComment.find(id)
    print(user_comment)
    return user_comment


async def find_user_comments():
    user_comments = await UserComment.findAll()
    for user_comment in user_comments:
        print(user_comment)
    return user_comments


async def delete_user_comment(id):
    user_comment = await UserComment.find(id)
    return await user_comment.remove()


async def update_user_comment(id, args):
    user_comment = await UserComment.find(id)
    for key, value in args.items():
        if hasattr(user_comment, key):
            setattr(user_comment, key, value)
    return await user_comment.change()

from models import *
from datetime import datetime


async def create_user_evaluation(args):
    user_evaluation = UserEvaluation()
    for key, value in args.items():
        if hasattr(user_evaluation, key):
            setattr(user_evaluation, key, value)
    return await user_evaluation.save()


async def find_user_evaluation(id):
    user_evaluation = await UserEvaluation.find(id)
    print(user_evaluation)
    return user_evaluation


async def find_user_evaluations():
    user_evaluations = await UserEvaluation.findAll()
    for user_evaluation in user_evaluations:
        print(user_evaluation)
    return user_evaluations


async def delete_user_evaluation(id):
    user_evaluation = await UserEvaluation.find(id)
    return await user_evaluation.remove()


async def update_user_evaluation(id, args):
    user_evaluation = await UserEvaluation.find(id)
    for key, value in args.items():
        if hasattr(user_evaluation, key):
            setattr(user_evaluation, key, value)
    return await user_evaluation.change()

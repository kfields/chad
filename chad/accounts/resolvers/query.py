from loguru import logger

#from django.contrib.auth.middleware import auser #Not published yet ...
from chad.schema.types.base import query
from chad.iam.middleware import get_request_user
from ..models import User
from ..schemata import UserConnection, UserEdge, UserNode

"""
@query.field("allUsers")
async def resolve_all_users(_, info, after:str=None, before:str=None, first:int=0, last:int=0):
    users = [u async for u in User.objects.all()]
    connection = UserConnection(users)
    result = connection.wire()
    return result
"""
@query.connection("allUsers")
async def resolve_all_users(_, info, after:str=None, before:str=None, first:int=0, last:int=0):
    users = [u async for u in User.objects.all()]
    return users

@query.field("user")
async def resolve_user(*_, id):
    return User.objects.aget(id=id)

@query.field("me")
async def resolve_me(_, info):
    user = await get_request_user(info.context["request"])
    #if user.is_authenticated:
    #    return user
    logger.debug(user)
    return user
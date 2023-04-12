from loguru import logger

from channels.db import database_sync_to_async
from django.utils.functional import SimpleLazyObject

from chad.schema.types.base import query
from ..models import User
from ..schema import UserConnection, UserEdge, UserNode


@query.field("allUsers")
async def resolve_all_users(_, info, after:str=None, before:str=None, first:int=0, last:int=0):
    #users = [u for u in User.objects.all()]
    users = [u async for u in User.objects.all()]
    connection = UserConnection(users)
    result = connection.wire()
    return result


@query.field("user")
async def resolve_user(*_, id):
    return User.objects.aget(id=id)


@database_sync_to_async
def get_request_user(request):
    if isinstance(request.user, SimpleLazyObject):
        request.user._setup()
    return request.user

@query.field("me")
async def resolve_me(_, info):
    #logger.debug(info.context["request"].__dict__)
    #user = info.context["request"].user
    user = await get_request_user(info.context["request"])
    #user = await get_user(info)
    #if user.is_authenticated:
    #    return user
    logger.debug(user)
    #return None
    return user
from loguru import logger

#from django.contrib.auth.middleware import auser #Not published yet ...
from chad.schema.types.base import query
from chad.iam.middleware import get_request_user
from ..models import Chat
from ..schema import ChatConnection, ChatEdge, ChatNode


@query.field("myChats")
async def resolve_my_chats(_, info, after:str=None, before:str=None, first:int=0, last:int=0):
    user = await get_request_user(info.context["request"])
    chats = [u async for u in Chat.objects.filter(user=user)]
    connection = ChatConnection(chats)
    result = connection.wire()
    return result


@query.field("chat")
async def resolve_chat(*_, id):
    return Chat.objects.aget(id=id)

@query.field("me")
async def resolve_me(_, info):
    user = await get_request_user(info.context["request"])
    #if user.is_authenticated:
    #    return user
    logger.debug(user)
    return user
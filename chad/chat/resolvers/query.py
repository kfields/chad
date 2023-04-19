from loguru import logger

from graphql_relay import from_global_id

#from django.contrib.auth.middleware import auser #Not published yet ...
from chad.schema.types.base import query
from chad.iam.middleware import get_request_user, get_request_avatar
from ..models import Chat, Message

@query.connection("myChats")
async def resolve_my_chats(_, info, after:str=None, before:str=None, first:int=0, last:int=0):
    #user = await get_request_user(info.context["request"])
    avatar = await get_request_avatar(info.context["request"])
    chats = [u async for u in avatar.chat_set.all()]
    return chats

@query.field("chat")
async def resolve_chat(*_, id):
    id = from_global_id(id)[1]
    logger.debug(id)
    return await Chat.objects.aget(id=id)

###
@query.connection("chatMessages")
async def resolve_chat_messages(*_, chatId, after:str=None, before:str=None, first:int=0, last:int=0):
    chatId = from_global_id(chatId)[1]
    chat = await Chat.objects.aget(id=chatId)
    messages = [u async for u in Message.objects.filter(chat=chat)]
    return messages

@query.field("message")
async def resolve_message(*_, id):
    id = from_global_id(id)[1]
    return await Message.objects.aget(id=id)

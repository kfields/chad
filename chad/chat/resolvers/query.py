from loguru import logger

#from django.contrib.auth.middleware import auser #Not published yet ...
from chad.schema.types.base import query
from chad.iam.middleware import get_request_user, get_request_avatar
from ..models import Chat, Message
from ..schemata import ChatConnection, MessageConnection


@query.field("myChats")
async def resolve_my_chats(_, info, after:str=None, before:str=None, first:int=0, last:int=0):
    #user = await get_request_user(info.context["request"])
    #chats = [u async for u in Chat.objects.filter(user=user)]
    avatar = await get_request_avatar(info.context["request"])
    chats = [u async for u in avatar.chat_set.all()]
    connection = ChatConnection(chats)
    result = connection.wire()
    return result


@query.field("chat")
async def resolve_chat(*_, id):
    return await Chat.objects.aget(id=id)

###

@query.field("chatMessages")
async def resolve_chat_messages(_, info, chatId, after:str=None, before:str=None, first:int=0, last:int=0):
    user = await get_request_user(info.context["request"])
    chat = await Chat.objects.aget(id=chatId)
    messages = [u async for u in Message.objects.filter(chat=chat)]
    connection = MessageConnection(messages)
    result = connection.wire()
    return result


@query.field("message")
async def resolve_message(*_, id):
    return Message.objects.aget(id=id)

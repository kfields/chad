from loguru import logger

#from channels.db import database_sync_to_async
from chad.schema.types.base import mutation
from chad.iam.middleware import get_request_user

from ..models import Chat, Message
from accounts.models import User

"""
@database_sync_to_async
def create_chat(user: User, title: str):
    chat = Chat(user=user, title=title)
    chat.save()
    return chat
"""

@mutation.field("createChat")
async def resolve_create_chat(_, info, input):
    user = await get_request_user(info.context["request"])
    if not user.is_authenticated:
        raise Exception("User not authenticated!")
    
    from_agent = user.avatar
    to_agent = input.get("to", None)
    name = input.get("name", None)

    chat = await Chat.objects.acreate(name=name, agents=[from_agent, to_agent])
    logger.debug(chat)
    return chat

@mutation.field("createMessage")
async def resolve_create_message(_, info, input):
    user = await get_request_user(info.context["request"])
    if not user.is_authenticated:
        raise Exception("User not authenticated!")

    chat_id = input.get("chatId", None)
    chat = await Chat.objects.aget(id=chat_id)
    role = input.get("role", None)
    content = input.get("content", None)

    message = await Message.objects.acreate(chat=chat, role=role, content=content) #Can't: causes validation error
    logger.debug(message)
    return message

@mutation.field("sendMessage")
async def resolve_create_message(_, info, input):
    user = await get_request_user(info.context["request"])
    if not user.is_authenticated:
        raise Exception("User not authenticated!")

    message_id = input.get("messageId", None)
    message = await Message.objects.aget(id=message_id)

    role = input.get("role", None)
    content = input.get("content", None)
    message = await Message.objects.acreate(chat=chat, role=role, content=content) #Can't: causes validation error
    logger.debug(message)
    return message

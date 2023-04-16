from loguru import logger

from channels.db import database_sync_to_async
from chad.schema.types.base import mutation
from chad.iam.middleware import get_request_user, get_request_avatar

from ..models import Chat, Message
#from accounts.models import User

from ..hub import hub

@database_sync_to_async
def create_chat(from_agent, to_agent):
    chat = Chat()
    chat.save()
    chat.agents.set([from_agent, to_agent])
    return chat

@mutation.field("createChat")
async def resolve_create_chat(_, info, input):
    """
    user = await get_request_user(info.context["request"])
    if not user.is_authenticated:
        raise Exception("User not authenticated!")
    """
    #from_agent = user.avatar
    from_agent = await get_request_avatar(info.context["request"])
    to_agent = input.get("to", None)

    #chat = await Chat.objects.acreate(agents=[from_agent, to_agent])
    chat = await create_chat(from_agent, to_agent)

    logger.debug(chat)
    return chat

@mutation.field("sendChatMessage")
async def resolve_send_chat_message(_, info, input):
    chat_id = input.get("id", None)
    from_agent = await get_request_avatar(info.context["request"])

    chat = await Chat.objects.aget(id=chat_id)

    content = input.get("content", None)

    message = await Message.objects.acreate(chat=chat, from_agent=from_agent, content=content) #Can't: causes validation error
    logger.debug(message)
    return message

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

"""
@mutation.field("sendMessage")
async def resolve_send_message(_, info, input):
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
"""

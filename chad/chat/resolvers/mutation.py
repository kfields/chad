from loguru import logger

from channels.db import database_sync_to_async
from chad.schema.types.base import mutation
from chad.iam.middleware import get_request_user

from ..models import Chat
from chad.iam.jwt import encode_auth_token
from accounts.models import User

@database_sync_to_async
def create_chat(user: User, title: str):
    chat = Chat(user=user, title=title)
    chat.save()
    return chat

@mutation.field("createChat")
async def resolve_create_chat(_, info, input):
    user = await get_request_user(info.context["request"])
    if not user.is_authenticated:
        raise Exception("User not authenticated!")

    title = input.get("title", None)

    #TODO:Fix this mess
    
    #post = await Post.objects.acreate(title=title, block=block, body=body) #Can't: causes validation error
    chat = await Chat.objects.acreate(user=user, title=title) #Can't: causes validation error

    #post = await sync_to_async(Post)(owner=user, title=title, block=block, body=body)

    logger.debug(chat)
    return chat

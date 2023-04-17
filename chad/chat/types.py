from channels.db import database_sync_to_async

from ariadne import ObjectType
from ariadne_relay import NodeObjectType

from .models import Chat, Message

from .events import chat_event_union

#user = ObjectType("User")
message = NodeObjectType("Message")

#chat = ObjectType("Chat")
chat = NodeObjectType("Chat")

# Add an instance_resolver to define how an instance of
# this type is retrieved, given an id
@chat.instance_resolver
async def resolve_chat_instance(id, *_):
    return await Chat.objects.aget(id=id)

@database_sync_to_async
def get_message_from(message):
    return message.from_agent

@message.field("from")
async def resolve_message_from(message, *_):
    return await get_message_from(message)
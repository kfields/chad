from pydantic import BaseModel

from ariadne import UnionType

from .models import Message

class ChatMessageEvent(BaseModel):
    id: int
    message: Message

    #TODO: define a validator for Message
    class Config:
        arbitrary_types_allowed = True

class ChatJoinEvent(BaseModel):
    id: int
    agent_id: int

class ChatLeaveEvent(BaseModel):
    id: int
    agent_id: int

def resolve_chat_event_type(obj, *_):
    if isinstance(obj, ChatMessageEvent):
        return "ChatMessageEvent"
    if isinstance(obj, ChatJoinEvent):
        return "ChatJoinEvent"
    if isinstance(obj, ChatLeaveEvent):
        return "ChatLeaveEvent"
    return None


chat_event_union = UnionType("ChatEvent", type_resolver=resolve_chat_event_type)

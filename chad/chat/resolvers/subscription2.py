import asyncio

from loguru import logger

from graphql.pyutils import SimplePubSubIterator

from chad.schema.types.base import subscription, pubsub

def transform_chat_event(event):
    logger.debug(event)
    return event

@subscription.subscription("chat")
def subscribe_chat(root, info, id):
    #return SimplePubSubIterator(pubsub, f"chat/{id}")
    return SimplePubSubIterator(pubsub, transform_chat_event)


@subscription.field("chat")
def push_chat_event(chat, info, id):
    logger.debug(chat)
    return chat

"""
from ..hub import hub, ChatSubscriber

@subscription.source("chat")
async def events_generator(obj, info, id=None):
    logger.debug(f'events_generator:begin:id {id}')
    subscriber = ChatSubscriber(int(id))
    hub.subscribe(subscriber)
    while subscriber.active:
        event = await subscriber.receive()
        logger.debug(f'events_generator:while:  {event}')
        yield event

@subscription.field("chat")
def events_resolver(event, info, id=None):
    logger.debug(f'events_resolver:while:  {event}')
    return event
"""
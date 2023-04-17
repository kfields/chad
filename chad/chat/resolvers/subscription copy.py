import asyncio

from loguru import logger

from chad.schema.types.base import subscription
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

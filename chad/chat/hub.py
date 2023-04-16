from ariadne import InterfaceType

from loguru import logger

#from hub import Hub, Subscriber, Event
from chad.schema.hub import Hub, Subscriber

hub = Hub()

chat_event = InterfaceType("ChatEvent")

@chat_event.type_resolver
def resolve_chat_event_type(obj, *_):
    #return obj.resolve_type()
    return obj.typename

class ChatSubscriber(Subscriber):
    def __init__(self, id):
        super().__init__()
        self.id = id

    async def send(self, msg):
        logger.debug(f'ChatSubscriber:send:  {msg.__dict__}')
        if msg.id != self.id:
            logger.debug(f'ChatSubscriber:send:no match:self:  {self.__dict__}')
            return
        await self.queue.put(msg)

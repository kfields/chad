from ariadne import InterfaceType

from loguru import logger

from chad.schema.hub import Hub, Subscriber

hub = Hub()

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

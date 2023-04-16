
from chad.message import Event

factories = None

class ChatEvent(Event):
    def __init__(self, id):
        super().__init__(id)

    @classmethod
    def produce(self, data):
        return factories[data['__typename']](data)

class ChatJoinEvent(ChatEvent):
    def __init__(self, id, playerId):
        super().__init__(id)
        self.player_id = playerId

class ChatMessageEvent(ChatEvent):
    def __init__(self, id, message):
        super().__init__(id)
        self.message = message

factories = {
    'ChatJoinEvent': lambda data: ChatJoinEvent(data['id'], data['agentId']),
    'ChatMessageEvent': lambda data: ChatMessageEvent(data['id'], data['message'])
}

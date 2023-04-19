from ariadne import InterfaceType

from chad.message import Event

factories = None

class ChatEvent(Event):
    def __init__(self, id):
        super().__init__(id)

    @classmethod
    def produce(self, data):
        return factories[data['__typename']](data)

class ChatJoinEvent(ChatEvent):
    def __init__(self, id, agent_id):
        super().__init__(id)
        self.agent_id = agent_id

class ChatLeaveEvent(ChatEvent):
    def __init__(self, id, agent_id):
        super().__init__(id)
        self.agent_id = agent_id

class ChatMessageEvent(ChatEvent):
    def __init__(self, id, message):
        super().__init__(id)
        self.message = message

chat_event = InterfaceType("ChatEvent")

@chat_event.type_resolver
def resolve_game_event_type(obj, *_):
    return obj.typename

factories = {
    'ChatJoinEvent': lambda data: ChatJoinEvent(data['id'], data['agentId']),
    'ChatLeaveEvent': lambda data: ChatLeaveEvent(data['id'], data['agentId']),
    'ChatMessageEvent': lambda data: ChatMessageEvent(data['id'], data['message'])
}

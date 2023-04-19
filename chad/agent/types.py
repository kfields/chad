from graphql_relay import to_global_id

from .models import Agent
"""
from ariadne import ObjectType

agent = ObjectType("Agent")
avatar = ObjectType("Avatar")
bot = ObjectType("Bot")
"""

from ariadne_relay import NodeObjectType


agent = NodeObjectType("Agent")

@agent.instance_resolver
async def resolve_agent_instance(id, *_):
    return await Agent.objects.aget(id=id)

avatar = NodeObjectType("Avatar")
bot = NodeObjectType("Bot")

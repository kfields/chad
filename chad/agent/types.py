"""
from ariadne import ObjectType

agent = ObjectType("Agent")
avatar = ObjectType("Avatar")
bot = ObjectType("Bot")
"""

from ariadne_relay import NodeObjectType


agent = NodeObjectType("Agent")
avatar = NodeObjectType("Avatar")
bot = NodeObjectType("Bot")

from loguru import logger

from graphql_relay import from_global_id

#from django.contrib.auth.middleware import auser #Not published yet ...
from chad.schema.types.base import query
from chad.iam.middleware import get_request_user
from ..models import User, Agent


@query.connection("allAgents")
async def resolve_all_agents(_, info, after:str=None, before:str=None, first:int=0, last:int=0):
    agents = [u async for u in Agent.objects.all()]
    return agents


@query.field("agent")
async def resolve_agent(*_, id):
    id = from_global_id(id)[1]
    return await Agent.objects.aget(id=id)

@query.field("myAvatar")
async def resolve_my_avatar(_, info):
    user = await get_request_user(info.context["request"])
    return user.avatar

@query.connection("myBots")
async def resolve_my_bots(_, info, after:str=None, before:str=None, first:int=0, last:int=0):
    user = await get_request_user(info.context["request"])
    bots = [u async for u in user.bot_set.all()]
    return bots

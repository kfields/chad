from loguru import logger

#from django.contrib.auth.middleware import auser #Not published yet ...
from chad.schema.types.base import query
from chad.iam.middleware import get_request_user
from ..models import User, Agent
from ..schemata import AgentConnection, AgentEdge, AgentNode


@query.field("allAgents")
async def resolve_all_agents(_, info, after:str=None, before:str=None, first:int=0, last:int=0):
    #users = [u for u in User.objects.all()]
    agents = [u async for u in Agent.objects.all()]
    connection = AgentConnection(agents)
    result = connection.wire()
    return result


@query.field("agent")
async def resolve_agent(*_, id):
    return Agent.objects.aget(id=id)

@query.field("myAvatar")
async def resolve_me(_, info):
    user = await get_request_user(info.context["request"])
    return user.avatar
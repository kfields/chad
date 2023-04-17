import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chad.settings')
import django
django.setup()
import asyncio

from ariadne import gql, ObjectType
from ariadne.executable_schema import make_executable_schema
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import include, re_path
from graphql.pyutils import SimplePubSub, SimplePubSubIterator
from graphql.subscription import subscribe

from .consumers import GraphQLHTTPConsumer, GraphQLWebsocketConsumer
from .subscription import SubscriptionAwareObjectType

from chad.schema import schema

from .asgi import application as django_application

application = ProtocolTypeRouter(
    {
        #"http": URLRouter([re_path(r"^graphql/$", GraphQLHTTPConsumer(schema).as_asgi(schema=schema))]),
        #"http": URLRouter([re_path(r"^graphql/$", django_application)]),
        "http": URLRouter([re_path(r"", django_application)]),
        "websocket": URLRouter(
            [re_path(r"^graphql/$", GraphQLWebsocketConsumer(schema).as_asgi(schema=schema))]
        ),
    }
)

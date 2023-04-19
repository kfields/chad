import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chad.settings')
import django
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import include, re_path

from .consumers import GraphQLHTTPConsumer, GraphQLWebsocketConsumer

from chad.schema import schema

from .asgi import application as django_application

application = ProtocolTypeRouter(
    {
        #"http": URLRouter([re_path(r"^graphql/$", GraphQLHTTPConsumer(schema).as_asgi(schema=schema))]),
        #"http": URLRouter([re_path(r"^graphql/$", django_application)]),
        "http": URLRouter([re_path(r"", django_application)]),
        "websocket": URLRouter(
            [re_path(r"^graphql/$", GraphQLWebsocketConsumer.as_asgi(schema=schema))]
        ),
    }
)

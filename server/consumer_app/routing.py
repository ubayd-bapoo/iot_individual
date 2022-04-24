from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from .websocket_consumers import WebsocketConsumer

websockets = URLRouter([
    path(
        "ws/sensehat/", WebsocketConsumer.as_asgi(),
        name="sensehat",
    ),
])

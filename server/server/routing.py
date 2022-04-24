from channels.routing import ProtocolTypeRouter, URLRouter
from consumer_app.routing import websockets

application = ProtocolTypeRouter({
    "websocket": websockets,
})

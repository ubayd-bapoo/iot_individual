# Built in imports.
import json

# Third Party imports.
from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer

# Django imports.
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser


class WebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self,):
        print(f'Connected to Websocket')
        await self.accept()

    async def receive(self, text_data):
        # when messages is received from websocket
        temperature = json.loads(text_data).get('temperature')
        print(temperature)
        await self.channel_layer.group_send('websocket_client',
                                            {"type": "websocket.send",
                                             "text": temperature})

    async def websocket_disconnect(self):
        # when websocket disconnects
        print("disconnected")

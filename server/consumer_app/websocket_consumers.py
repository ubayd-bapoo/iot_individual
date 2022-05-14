import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import SensehatReading


class WebsocketConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def write_db(self, sensehat_sensor=0, source=1, reading=''):
        obj = SensehatReading.objects.get_or_create(sensehat_sensor=sensehat_sensor, source=source, reading=reading)[0]
        obj.save()

    async def connect(self,):
        print(f'Connected to Websocket')
        await self.accept()

    async def receive(self, text_data):
        # when messages is received from websocket
        websocket_data = json.loads(text_data)
        print(f'Reading Websocket data: {websocket_data}')

        try:
            print("Saving Websocket to DB")
            await self.write_db(sensehat_sensor=0, source=1, reading=websocket_data['temperature'])
        except:
            print("Error Saving Websocket to DB")
            pass

        await self.channel_layer.group_send('websocket_client',
                                            {"type": "websocket.send",
                                             "text": websocket_data['temperature']})

    async def disconnect(self, text_data):
        # when websocket disconnects
        print("disconnected")

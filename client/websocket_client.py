import asyncio
import json
import time
import websockets

from sense_emu import SenseHat


HOST = '10.0.2.2'
PORT = 8000


async def start_sensehat(host: str, port: int) -> None:
    sense = SenseHat()
    stored_temperature = round(sense.get_temperature(), 0)

    async with websockets.connect(f"ws://{host}:{port}/ws/sensehat/") as ws:
        while True:
            temperature = round(sense.get_temperature(), 0)
            if temperature != stored_temperature:
                stored_temperature = temperature
                if temperature > 34:
                    message = {'temperature': temperature, 'type': 'hot'}
                    print(f'Writing Message {message}')
                    await ws.send(json.dumps(message))
                elif 34 > temperature > 24:
                    message = {'temperature': temperature, 'type': 'medium'}
                    print(f'Writing Message {message}')
                    await ws.send(json.dumps(message))
                else:
                    message = {'temperature': temperature, 'type': 'cold'}
                    print(f'Writing Message {message}')
                    await ws.send(json.dumps(message))
                time.sleep(3)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_sensehat(HOST, PORT))

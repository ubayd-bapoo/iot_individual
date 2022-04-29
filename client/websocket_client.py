import asyncio
import json
import time
import websockets

from sense_emu import SenseHat


HOST = '10.0.2.2'
PORT = 8000

async def produce(message: str, host:str, port: int) -> None:
    async with websockets.connect(f"ws://{host}:{port}/ws/sensehat/") as ws:
        await ws.send(message)
        await ws.recv()
        await ws.disconnect()

def start_sensehat():
    sense = SenseHat()
    stored_temperature = round(sense.get_temperature(), 0)

    while True:
        temperature = round(sense.get_temperature(), 0)
        if temperature != stored_temperature:
            stored_temperature = temperature
            if temperature > 34:
                message = {'temperature': temperature, 'type': 'hot'}
                print(f'Writing Message {message}')
                asyncio.run(produce(json.dumps(message), HOST, PORT))
            elif 34 > temperature > 24:
                message = {'temperature': temperature, 'type': 'medium'}
                print(f'Writing Message {message}')
                asyncio.run(produce(json.dumps(message), HOST, PORT))
            else:
                message = {'temperature': temperature, 'type': 'cold'}
                print(f'Writing Message {message}')
                asyncio.run(produce(json.dumps(message), HOST, PORT))
            time.sleep(3)


if __name__ == "__main__":
    start_sensehat()

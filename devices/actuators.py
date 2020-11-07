import random
import websockets
import asyncio
import random
import json


class Actuator:

    def __init__(self, id_, ty):
        self.id = id_
        self.ty = ty

    async def start_listen(self):
        uri = "ws://localhost:8765"

        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({'id': self.id}))

            consumer_task = asyncio.ensure_future(
                self.consume(websocket))
            producer_task = asyncio.ensure_future(
                self.produce(websocket))
            await asyncio.wait([consumer_task, producer_task])

    async def consume(self, ws):
        async for message in ws:
            print("Received message from api: ", message)

    async def produce(self, ws):
        while True:
            await asyncio.sleep(5)
            data = self.measure()
            if data is None:
                continue
            await ws.send(json.dumps({'id': self.id, 'data': data}))

    def measure(self):

        # define whether a measurement has happened
        measurement_happened = random.choice([True, False])

        if measurement_happened:

            if self.ty == 'doorlock':
                # smart door lock: locked, unlocked
                return random.choice([False, True])

            elif self.ty == 'lamp':
                # smart lamp: continous value [0,1]
                return random.uniform(0, 1)
        else:
            return None

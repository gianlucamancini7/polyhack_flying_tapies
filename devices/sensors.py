import random
import websockets
import json
import asyncio

# import configurations
from configuration import id_1, id_2, id_3, id_4


class Sensor:

    def __init__(self, id_, ty):
        self.id = id_
        self.ty = ty

    async def start_listen(self):
        uri = "ws://localhost:8765"

        async with websockets.connect(uri) as websocket:

            while True:
                data = {
                    "id": self.id,
                    "data": self.measure()
                }

                await websocket.send(json.dumps(data))
                await asyncio.sleep(5)

    def measure(self):

        # define whether a measurement has happened
        measurement_happened = random.choice([True, False])

        if measurement_happened:

            if self.ty == 'motion' or self.ty == 'noise':
                # motion sensor: no_motion, motion
                return random.choice([False, True])

            elif self.id == 'proximity':
                # distance sensor: real value between 0 and 30 m
                return random.uniform(0, 30)

        # sensor sends no data
        else:
            return None

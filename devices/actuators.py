import random
import websockets
import asyncio
import random
import json

#import configurations
from configuration import id_5, id_6, id_7


class Actuator:

    def __init__(self, id_, ty):
        self.id = id_
        self.ty = ty

    async def start_listen(self):
        uri = "ws://localhost:8765"

        async with websockets.connect(uri) as websocket:
            while True:
                data = self.measure()
                await websocket.send(json.dumps(data))
                await asyncio.sleep(5)

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

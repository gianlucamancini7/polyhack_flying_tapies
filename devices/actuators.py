import random

#import configurations
from configuration import id_5, id_6, id_7


class Actuator:

    def __init__(self, id_):
        self.id = id_

    async def start_listen():
        uri = "ws://localhost:8765"

        async with websockets.connect(uri) as websocket:

            data = self.measure()
            # data={'id': '69420', 'data': 1234}

            while True:
                await websocket.send(json.dumps(data))
                await asyncio.sleep(5)

    def measure(self):

        # define whether a measurement has happened
        measurement_happened = random.choice(True, False)

        if measurement_happened:

            if self.id == id_5:
                # smart door lock: locked, unlocked
                return random.choice(False, True)

            elif self.id == id_6:
                # smart lamp: continous value [0,1]
                return random.uniform(0, 1)

            elif self.id == id_7:
                # smart lamp: continous value [0,1]
                return random.uniform(0, 1)

        else:
            return None

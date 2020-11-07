import random

# import configurations
from configuration import id_1, id_2, id_3, id_4


class Sensor:

    def __init__(self, id_):
        self.id = id_

    async def start_listen():
        uri = "ws://localhost:8765"

        async with websockets.connect(uri) as websocket:

            data = {
                "id": self.id,
                "data": self.measure()
            }

            # data={'id': '69420', 'data': 1234}

            while True:
                await websocket.send(json.dumps(data))
                await asyncio.sleep(5)

    def measure(self):

        # define whether a measurement has happened
        measurement_happened = random.choice(True, False)

        if measurement_happened:

            if self.id == id_1:
                # motion sensor: no_motion, motion
                return random.choice(False, True)

            elif self.id == id_2:
                # smart noise sensor: no suspicious noise, suspicious noise detected
                return random.choice(False, True)

            elif self.id == id_3:
                # distance sensor: real value between 0 and 30 m
                return random.uniform(0, 30)

            elif self.id == id_4:
                # distance sensor: real value between 0 and 30 m
                return random.uniform(False, True)

        # sensor sends no data
        else:
            return None

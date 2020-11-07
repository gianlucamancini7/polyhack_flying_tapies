import random

class Actuator:
    
    def __init__(self, id_):
        self.id=id_

    async def start_listen():
        uri = "ws://localhost:8765"

        async with websockets.connect(uri) as websocket:

            data=self.measure()
            # data={'id': '69420', 'data': 1234}

            while True:
                await websocket.send(json.dumps(data))
                await asyncio.sleep(5)

    def measure(self):

        #define whether a measurement has happened
        measurement_happened=random.choice([True, False])

        if measurement_happened:

            if self.id:
                return random.choice([no_motion, motion])

            elif self.id:
                return random.choice([no_motion, motion])

        else:
            return None
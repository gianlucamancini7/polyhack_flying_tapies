import asyncio
import websockets
import logging
import json

from simulate import simulation


logging.basicConfig()


async def executeMessage():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # await websocket.send("Hello world!")
        # await simulation(websocket)
        while True:
            await websocket.send(json.dumps({'id': '69420', 'data': 1234}))
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(executeMessage())

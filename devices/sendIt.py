import asyncio
import websockets

from simulate import simulation

async def executeMessage():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")
        await simulation()
        
if __name__ == "__main__":

    asyncio.get_event_loop().run_until_complete(executeMessage())
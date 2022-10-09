import asyncio
import websockets


async def solution() -> None:
    uri = "ws://socket.mirea.ninja:8000/"
    async with websockets.connect(uri) as websocket:
        await websocket.send('{"key": "aw3s0m3_k3y"}')
        print(await websocket.recv())


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run(solution())

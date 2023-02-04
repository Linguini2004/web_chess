import asyncio

import websockets

fen_string = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

async def handler(websocket):
    # send fen string
    await websocket.send(fen_string)
    print("server sent", fen_string)
    while True:
        
        
        try:
            message = await websocket.recv()
        except websockets.ConnectionClosedOK:
            break
        # else:
        #     await websocket.send(message) to be continued
        print("the server recieved", message)

        await websocket.send(message)
        print("the server sent", message)
        # await websocket.send(message) => echos what is sent by front end


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
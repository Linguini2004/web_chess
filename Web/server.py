import http.server
import ws
import asyncio
import websockets
import subprocess

HandlerClass = http.server.SimpleHTTPRequestHandler

# Patch in the correct extensions
HandlerClass.extensions_map['.js'] = 'text/javascript'
HandlerClass.extensions_map['.mjs'] = 'text/javascript'

subprocess.run(["python", "./ws.py"])

http.server.test(HandlerClass, port=8000)



'''
async def main():
    #ws_server = asyncio.create_task(ws.main())

    # Run the server (like `python -m http.server` does)
    #http_server = asyncio.create_task(http.server.test(HandlerClass, port=8000))

    #await ws_server
    #await http_server

    #await asyncio.gather(ws_server, http_server)
    #await ws.main()

    #await http.server.test(HandlerClass, port=8000)
    #await asyncio.gather(ws.main(), http.server.test(HandlerClass, port=8000))

    #await asyncio.gather(start_ws(), http.server.test(HandlerClass, port=8000))

    await start_ws()

    #await asyncio.Future()

async def start_ws():
    async with websockets.serve(ws.handler, "", 8001, ping_timeout=None):
        print("Started web server on port 8001")
        await start_http()
        #await asyncio.Future()

async def start_http():
    async with http.server.test(HandlerClass, port=8000):

        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
'''
# 这是用asyncio写的
from socket import *
import asyncio
import test20maybeend3

loop = asyncio.get_event_loop()
# loop = test20maybeend3.Loop()  # it should be same as last line

async def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    sock.setblocking(False)
    while True:
        client, addr = await loop.sock_accept(sock)
        print('Connention from', addr)
        loop.create_task(echo_handler(client))


async def echo_handler(client):
    with client:
        while True:
            data = await loop.sock_recv(client, data)
            if not data:
                break
            await loop.sock_sendall(client, b'Server got' + data)
    print('Connentino closed.')

loop.create_task(echo_server(('', 25000)))
loop.run_forever()
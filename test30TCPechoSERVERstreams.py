import asyncio

async def abc(reader, writer):
    da = await reader.readline()
    print('server received:', da.decode())
    writer.write('You have connented...\n'.encode())
    await writer.drain()
    writer.close()

loop = asyncio.get_event_loop()
co = asyncio.start_server(abc, '127.0.0.1', 12345, loop=loop)
ser = loop.run_until_complete(co)
print("{} is waiting for client connenting".format(ser.sockets[0].getsockname()))
try:
    loop.run_forever()
except:
    pass

ser.close()
loop.run_until_complete(ser.wait_closed())
loop.close()
# -----------------------------------------------------
# import asyncio
#
#
# @asyncio.coroutine
# def handle_echo(reader, writer):
#     data = yield from reader.read(100)
#     message = data.decode()
#     addr = writer.get_extra_info('peername')
#     print("Received %r from %r" % (message, addr))
#
#     print("Send: %r" % message)
#     writer.write(data)
#     yield from writer.drain()
#
#     print("Close the client socket")
#     writer.close()
#
# loop = asyncio.get_event_loop()
# coro = asyncio.start_server(handle_echo, '127.0.0.1', 8888, loop=loop)
# server = loop.run_until_complete(coro)
#
# # Serve requests until Ctrl+C is pressed
# print('Serving on {}'.format(server.sockets[0].getsockname()))
# try:
#     loop.run_forever()
# except KeyboardInterrupt:
#     pass
#
# # Close the server
# server.close()
# loop.run_until_complete(server.wait_closed())
# loop.close()
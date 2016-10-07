import asyncio

async def cli(mess, lo):
    re, wi = await asyncio.open_connection('127.0.0.1', 12345, loop=lo)
    wi.write(mess.encode())
    # da = await re.readline()
    # print("CLIENT received:", da.decode())
    wi.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(cli('asdfdfgb\n', loop))
loop.close()
# ------------------------------------------------------
# import asyncio
#
#
# @asyncio.coroutine
# def tcp_echo_client(message, loop):
#     reader, writer = yield from asyncio.open_connection('127.0.0.1', 8888,
#                                                         loop=loop)
#
#     print('Send: %r' % message)
#     writer.write(message.encode())
#
#     data = yield from reader.read(100)
#     print('Received: %r' % data.decode())
#
#     print('Close the socket')
#     writer.close()
#
# message = 'Hello World!'
# loop = asyncio.get_event_loop()
# loop.run_until_complete(tcp_echo_client(message, loop))
# loop.close()
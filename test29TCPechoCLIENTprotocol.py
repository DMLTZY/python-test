import asyncio


class E(asyncio.Protocol):
    def __init__(self, mess, loo):
        self.message = mess
        self.loop = loo

    def connection_made(self, transport):
        transport.write(self.message.encode())

    def data_received(self, data):
        print("client received: {}".format(data.decode()))

    def connection_lost(self, exc):
        print("server closed")
        self.loop.stop()

loop = asyncio.get_event_loop()
co = loop.create_connection(lambda: E('afasd', loop), '127.0.0.1', 12345)
loop.run_until_complete(co)
loop.run_forever()
loop.close()
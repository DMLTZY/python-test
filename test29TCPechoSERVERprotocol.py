import asyncio


class Echo(asyncio.Protocol):
    def connection_made(self, transport):
        peer = transport.get_extra_info("peername")
        print("{} connented".format(peer))
        self.trans = transport

    def data_received(self, data):
        print("client send me: {}".format(data.decode()))
        self.trans.write('Hi client, I got your message'.encode())


loop = asyncio.get_event_loop()
co = loop.create_server(Echo, '127.0.0.1', 12345)
serv = loop.run_until_complete(co)
try:
    loop.run_forever()
except:
    pass

serv.close()
loop.run_until_complete(serv.wait_closed())
loop.close()

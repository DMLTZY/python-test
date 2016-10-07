import asyncio
import random
import time


async def aa():
    for _ in range(3):
        return '*'


async def dosomething(num, loop):
    print("I am {}.".format(num))
    a = 0
    if num == 1:
        a = 3
    elif num == 2:
        a = 0.1
    await aa()
    print("{} is awake".format(num))


loop = asyncio.get_event_loop()

asyncio.ensure_future(dosomething(1, loop))
asyncio.ensure_future(dosomething(2, loop))
asyncio.ensure_future(dosomething(3, loop))
asyncio.ensure_future(dosomething(4, loop))

loop.run_forever()
loop.close()
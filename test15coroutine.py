# https://docs.python.org/3/library/asyncio-task.html
# import asyncio
# import datetime
#
# async def display(loop):
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(display(loop))
# loop.close()
# ---------------------------------------------
# import asyncio
#
# async def compute(x, y):
#     print('Compute {} + {} ...'.format(x, y))
#     await asyncio.sleep(1.0)
#     return x + y
#
# async def print_sum(x, y):
#     result = await compute(x, y)
#     print('{} + {} = {}'.format(x, y, result))
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(print_sum(1, 2))
# print('ending.....')
# loop.close()
# ---------------------------------------------
# import asyncio
#
# async def slow_operation(future):
#     await asyncio.sleep(2)
#     future.set_result('Future is done.....')
#
# loop = asyncio.get_event_loop()
# future = asyncio.Future()
# asyncio.ensure_future(slow_operation(future))
# loop.run_until_complete(future)
# print(future.result())
# loop.close()
# ---------------------------------------------
# import asyncio
#
# async def slow_operation(future):
#     await asyncio.sleep(1)
#     future.set_result('Future is done.....')
#
# def got_result(future):
#     print(future.result())
#     loop.stop()
#
# loop = asyncio.get_event_loop()
# future = asyncio.Future()
# asyncio.ensure_future(slow_operation(future))
# future.add_done_callback(got_result)
# try:
#     loop.run_forever()
# finally:
#     loop.close()
# ---------------------------------------------
import asyncio, random, time

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print('Task {} and {} is received, it will be dealed...'.format(name, i))
        await ran()
        f *= i
    print('Task {} is finished, the result is {}.'.format(name, f))

async def ran():
    print('I need to sleep some seconds...')
    sl = random.random() * 2
    await asyncio.sleep(sl)
    print('it costs {}'.format(sl))

loop = asyncio.get_event_loop()
task = [
    asyncio.ensure_future(factorial('A', 2)),
    asyncio.ensure_future(factorial('B', 3)),
    asyncio.ensure_future(factorial('C', 4)),
    asyncio.ensure_future(factorial('D', 2)),
    asyncio.ensure_future(factorial('E', 3)),
    asyncio.ensure_future(factorial('F', 4)),
]
loop.run_until_complete(asyncio.gather(*task))
print('end......')
loop.close()
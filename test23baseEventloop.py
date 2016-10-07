import asyncio
from datetime import datetime
from functools import partial


def display_date(endtime, loop):
    print('Now, it is {}.'.format(datetime.now()))
    if (loop.time() + 1.0) <= endtime:
        print('You will be delay 1 second.')
        loop.call_later(1, partial(display_date, endtime, loop))
    else:
        print('I will stop.')
        loop.stop()

loop = asyncio.get_event_loop()
endtime = loop.time() + 3
loop.call_soon(partial(display_date, endtime, loop))
loop.run_forever()
loop.close()

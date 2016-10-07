import asyncio


@asyncio.coroutine
def slow_operation():
    """
    This coroutine *returns* an eventual result.
    """
    # Imagine a pause from some non-blocking network based I/O here.
    yield from asyncio.sleep(1)
    # A *lot* more conventional and no faffing about with future instances.
    return 'A return value from the slow_operation coroutine!'


def got_result(future):
    """
    This function is a callback. Its only argument is a resolved future
    whose result it prints. It then causes the event loop to stop.

    In this example, the resolved future is, in fact, a Task instance.
    """
    print(future.result())
    loop.stop()


# Get the instance of the event loop (also referenced in got_result).
loop = asyncio.get_event_loop()
# Wrap the coroutine in a task to schedule it for execution when the event
# loop starts.
task = asyncio.Task(slow_operation())
# Add the callback to the task. The callback will only be executed when the
# task is resolved by the coroutine. The task object is passed into the
# got_result callback.
task.add_done_callback(got_result)

# Run the event loop until loop.stop() is called (in got_result).
try:
    loop.run_forever()
finally:
    loop.close()
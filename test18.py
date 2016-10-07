
def coroutine(func):
    def wrapper(*args, **kwargs):
        return next(func(*args, **kwargs))
    return wrapper


def follow(thefile, target):
    next(target)
    while True:
        target.send(thefile)


#@coroutine
def printer():
    print('printer...')
    while True:
        line = (yield)
        print(line)


#@coroutine
def grep(pattern, target):
    print('grep...')
    next(target)
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


def broadcast(targets):
    while True:
        item = yield
        for target in targets:
            next(target)
            target.send(item)

p = printer()
follow('aa241', broadcast([grep('a', p), grep('1', p),]))
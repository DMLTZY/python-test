import time


def gen1():
    yield 'a'
    yield 'b'
    yield 'c'


def gen2():
    for c in gen1():
        yield c
    yield 'd'
    yield 'e'


def gen3():
    yield from gen1()
    yield 'd'
    yield 'e'


def gen4():
    # yield '1'
    yield '2'
    return '3'


def gen5():
    val = yield from gen4()
    yield val + '4'
    yield '5'


for g in gen5():
    print(g)
    #time.sleep(2)

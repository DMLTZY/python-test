def consumer(func):
    def wrapper(*args, **kw):
        gen = func(*args, **kw)
        next(gen)
        return gen
    wrapper.__name__ = func.__name__
    wrapper.__dict__ = func.__dict__
    wrapper.__doc__ = func.__doc__
    return wrapper


def aa():
    print('In aa()')
    result = yield '(from aa)'
    print('You put {} in aa()'.format(result))
    return 'return aa'

#
#
# a = aa()
# try:
#     a.send(12341234)
# except:
#     pass
def cc():
    print('In cc()')
    while 1:
        rec = yield from aa()
        print('cc get {} from aa'.format(rec))
    #return 'return cc'

def dd():
    return 'In dd()'

@consumer
def bb():
    print('In bb()')
    try:
        resultb = yield from dd()  # aa(), cc(), dd()
        print('In bb', resultb)
    except:
        print('EXCEPTION IN bb()')
        pass
    else:
        print('{} get from aa()'.format(resultb))
        reb = yield 'Close aa()'
        print('bb get {} from main'.format(reb))

b = bb()
try:
    for _ in range(3):
        a = b.send(1234)
        print(a)
except StopIteration:
    print('stopiteration exit.....')
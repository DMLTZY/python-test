# def consumer():
#     rr = ''
#     while True:
#         nn = yield rr
#         if not nn:
#             return
#         print('[CONSUMER] Consuming %s...' % nn)
#         rr = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n += 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)
# -----------------------------------------------------------------
def h():
    print('launch...')
    m = yield 2
    print('h() get: ({})'.format(m))
    d = yield 434
    print('func end.')


c = h()
b = c.send(None)
print('get ({}) from func.'.format(b))
a = c.send('input..')
print('get ({}) from func.'.format(a))
try:
    c.send(None)
except:
    pass


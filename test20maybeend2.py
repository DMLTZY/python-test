
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# for i in countdown(5):
#     print(i)
# -------------------------------------------------
from types import coroutine
@coroutine
def spam():
    result = yield 'somevalue'
    print('The result is', result)

# f = spam()
# print(f.send(None))
# print(f.send(123))
# -------------------------------------------------
async def foo():
    print('Start foo')
    await spam()
    print('End foo')

# f = foo()
# print(f.send(None))
# print(f.send(34))
# -------------------------------------------------
async def bar():
    print('Start bar')
    await foo()
    print('End bar')

f = bar()
print(f.send(None))
try:
    print(f.send(23))
except:
    pass
import functools


def log(*args):
    def decorate(func):
        def wrapper(*args2, **kwargs):
            if args:
                print('You have inputed {} argument'.format(len(args)))
                print('They are: ', args)
            else:
                print('There is no argument')
            print(func.__name__)
            return func(*args2, **kwargs)
        return wrapper
    return decorate


@log()
def a():
    print('--> I don\'t have argument.')


@log('ag1', 'gh')
def b():
    print('--> I have some arguments.')

#a()
#b()
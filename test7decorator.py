from functools import wraps


def ww(text):
    def decorate(func):
        def wrapper(*args, **kwargs):
            wrapper.__name__ = text.__name__
            return func(*args, **kwargs)
        return wrapper
    return decorate


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('BEGIN LOGGING...')
        func(*args, **kwargs)
        print('END LOGGING...')
        return None
    return wrapper


@log
def pp():
    print("test")


pp()

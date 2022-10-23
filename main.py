from debug_tools import debug_decorator, timer

@debug_decorator
def foo():
    x = 1
    return x

@debug_decorator
def foo2():
    x = 2
    return x

@debug_decorator
@timer
def summator(a,b):
    return a**b


if __name__ == '__main__':
    foo()
    foo2()
    summator(2, 100)


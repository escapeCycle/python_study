# -*- coding: utf-8 -*-
# 装饰器
import functools, time


def now():
    print('2019-09-24')


f = now
f()
print(now.__name__)
print(f.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 把@log放到now()函数的定义处，相当于执行了语句 now = log(now)
@log
def now2():
    print('2019-09-25')


now2()
print(now2.__name__)


# 如果decorator本身需要传入参数
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：now3 = log2('execute')(now)
@log2('execute')
def now3():
    print('2019-09-25')


now3()
print(now3.__name__)  # 函数名称会变成 wrapper，所以需要把原始的函数名复制到wrapper中，否则会有问题


def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log3
def now4():
    print('2019-09-25')


print(now4.__name__)


@log4('execute')
def now5():
    print('2019-09-25')


print(now5.__name__)


# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        func = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return func

    return wrapper


# 测试 metric(fast)
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


# metric(slow)
@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
print(fast.__name__)
print(slow.__name__)
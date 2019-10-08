# -*- coding: utf-8 -*-

L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))


def fib(n):
    num, a, b = 0, 0, 1
    while num < n:
        c = b
        a, b = b, a + b
        num = num + 1
    return c


print(fib(6))


# 使用yield 会得到一个generator
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


y = fib2(6)
print(y)
for n in y:
    print(n)

g = fib2(6)
while True:
    try:
        x = next(g)
        print('g: ', x)
    except StopIteration as e:
        print('Generator return value : ', e.value)
        break


# yield 用法
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


d = odd()
print(next(d))
print(next(d))
print(next(d))

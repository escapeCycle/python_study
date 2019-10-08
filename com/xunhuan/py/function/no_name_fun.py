# -*- coding: utf-8 -*-
# 匿名函数 lambda

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

f = lambda x: x * x
print(f)
print(f(5))


# build1 和 build2 等价
def build1(x, y):
    def f():
        return x * x + y * y

    return f


# 闭包
def build2(x, y):
    return lambda: x * x + y * y


print(build1(2, 3))
print(build1(2, 3)())
print(build2(2, 3))
print(build2(2, 3)())


def is_odd(n):
    return n % 2 == 1


# 使用lambda改造下面函数
L = list(filter(is_odd, range(1, 20)))
L1 = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(L)
print(L1)

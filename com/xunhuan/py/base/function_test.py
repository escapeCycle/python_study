# -*- coding: utf-8 -*-
from abstest import my_abs
import math

print(abs(-10))
print(max(1, 2, 3, -1, 2, 4, 100))
print(hex(100))

# 自定义函数
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x


print(my_abs(-100))


# 定义两个返回的函数
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 使用函数
x, y = move(100, 100, 60, math.pi / 6)

print(x, y)


# 给定默认值 n = 2，n可不必须传，兼容老代码
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5,2))
print(power(5))
print(power(5,3))

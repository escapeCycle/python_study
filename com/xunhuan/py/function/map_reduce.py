# -*- coding: utf-8 -*-
from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])  # 返回的是iterator
# print(next(r))
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6])))


def add(x, y):
    return x + y


# reduce 用法 reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
rr = reduce(add, [1, 3, 5, 7, 9])
print(rr)


def fn(x, y):
    return x * 10 + y


rrr = reduce(fn, [1, 2, 3, 4, 5])
print(rrr)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# 字符转数字
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return DIGITS[s]


print(reduce(fn, map(char2num, '13579')))


def char2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(char2int('12345'))


# 首字母边小写
def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 计算L中所有数的乘机
def prod(L):
    def multiply(x, y):
        return x * y

    return reduce(multiply, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 字符转成浮点数 把字符串'123.456'转换成浮点数123.456
def str2float(s):
    s_left = s.split('.')[0]
    s_right = s.split('.')[1]

    def char2num(s):
        return DIGITS[s]

    def fn(x, y):
        return x * 10 + y

    return reduce(fn, map(char2num, s_left)) + reduce(fn, map(char2num, s_right)) / pow(10, len(str(s_right)))


print(str2float('123.456'))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
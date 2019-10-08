# -*- coding: utf-8 -*-
def is_odd(x):
    return x % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))


def not_empty(x):
    return x and x.strip()


print(list(filter(not_empty, ['', 'A', 'B', None, '   '])))


def add(x):
    return x + 5


print(list(filter(add, [1, 2, 3, 4, 5])))


# 打印出所有素数
# 从3开始的奇数序列，无限序列
def odd_iter():
    r = 1
    while True:
        r = r + 2
        yield r


def not_divisible(ss):
    return lambda x: x % ss > 0


def primes():
    yield 2
    it = odd_iter()
    while True:
        nn = next(it)
        yield nn
        it = filter(not_divisible(nn), it)


# 打印素数
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


# 筛选是否是回数 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(xxn):
    if len(str(xxn)) == 1:
        return True
    else:
        ln = list(str(xxn))
        num = 0
        num2 = -1
        for r in ln:
            if ln[num] != ln[num2]:
                return False
            num = num + 1
            num2 = num2 - 1
            if num > len(str(xxn)) / 2:
                return True


def is_palindrome2(n):
    return str(n) == str(n)[::-1]  # 从后向前每一个都取


# 测试:
output = filter(is_palindrome2, range(1, 1000))
print('1~1000:', list(output))

if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

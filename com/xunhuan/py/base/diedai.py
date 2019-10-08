# -*- coding: utf-8 -*-
from collections import Iterator
from collections.abc import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key, value in d.items():
    print(key, value)
print('-------')
for key in d:
    print(key, d.get(key))
print('-------')
for ch in 'ABC':
    print(ch)

# 判断是否可以迭代
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))
print('-------')
# 带下标
for index, item in enumerate(list([2, 3, 4, 5, 6, 7])):
    print(index, item)
print('-------')
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)

cc = iter(['1', '2', '3'])  # 使用iter转换成迭代器类型
print(isinstance(cc,Iterator))


# 练习
def findMinAndMax(L):
    return max(L), min(L)


print(findMinAndMax([1, 4, 100, 2]))

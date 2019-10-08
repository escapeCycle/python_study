# -*- coding: utf-8 -*-
print(sorted([-20, 19 - 20, 2, 9, 100]))

# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
print(sorted([-20, 19 - 20, 2, 9, 100], key=abs))

# 转小写之后排序
print(sorted(['tianH1', 'Tianh2', 'Lvdd1', 'LVDD2'], key=str.lower))

# 转小写之后排序 倒排
print(sorted(['tianH1', 'Tianh2', 'Lvdd1', 'LVDD2'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


# 根据名字排序
L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return -t[1]


# 根据分数排序 从高到低
L2 = sorted(L, key=by_score)
print(L2)

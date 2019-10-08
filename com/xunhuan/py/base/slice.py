# -*- coding: utf-8 -*-
L = ['tianh1', 'tianh2', 'lvdd1', 'lvdd2']

r = []
n = 4
for i in range(n):
    r.append(L[i])

print(r)

print(L[0:3])
print(L[:3])  # 同上
print(L[1:3])
print(L[-1:])

L = list(range(100))
print(L[::5])  # 每隔5个取一个
print(L[0:10:2])  # 前十个数,每两个取一个

print('ABCDEFG'[:3])  # 类似于substring
print('ABCDEFG'[0:0:2])
# -*- coding: utf-8 -*-

# 列表生成式
print([x * x for x in range(1, 11)])

print([
    x * x for x in range(1, 11) if x % 2 == 0
])

print([
    m + n for m in 'ABC' for n in 'XYZ'
])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([
    k + '=' + v for k, v in d.items()
])

# 练习
L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s, str)]

print(L2)

L3 = []
for x in L1:
    if isinstance(x, str):
        y = x.lower()
        L3.append(y)
    else:
        L3.append(x)
print(L3)

L4 = [s.lower() for s in [str(y) for y in L1]]
print(L4)

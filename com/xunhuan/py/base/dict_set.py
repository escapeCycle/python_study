# -*- coding: utf-8 -*-

# 和list相比 dict有以下特点(用空间换取时间)
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
d = {'tianh1': 95, 'tianh2': 99, 'lvdd': 30}

print(d['tianh1'])

d['tianh2'] = 100

print(d['tianh2'])
print(d)

if 'tianh2' in d:
    print('yes')
else:
    print('no')

print(d.get('tianh1'))

# 删除
d.pop('tianh2')

print(d)

# set

s = set([1, 2, 3])
print(s)
# 不会有重复元素
s = set([1, 1, 2, 2, 3])
print(s)
s.add(4)
s.remove(2)
print(s)

# 交集 并集
s1 = {3, 1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)
print(s1 | s2)

a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)

a = 'abc'
b = a.replace('a', 'A')
print(a)
print(b)

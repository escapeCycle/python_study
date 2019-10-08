# -*- coding: utf-8 -*-
# for 练习
names = ['tianh', 'tianh2', 'tianh3', 'lvdd']

for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

print(list(range(5)))

# 同上
sum = 0
for x in range(11):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
   sum = sum + n
   n = n - 2
print(sum)

print('START')
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

print('START2')
n = 0
while n <= 10:
    n = n + 1
    if n % 2 == 0:  # 如果是偶数，执行continue
        continue
    print(n)
print('END2')
# -*- coding: utf-8 -*-
# 杨辉三角 可以记住上一个list的值 preList = []  cur = preList[i-1] + preList[i]
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
L = [1]


def triangles():
    for n in range(10):
        yield list(L)
        for i in range(1, len(L)):
            L[-i] = L[-i] + L[-i - 1]   # 等于原值加前一个值
        L.append(1)


for x in triangles():
    print(x)

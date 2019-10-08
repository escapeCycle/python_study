# -*- coding: utf-8 -*-
# 偏函数 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
import functools

print(int('12345', base=8))  # 转换成int 8进制 转成10进制
print(int('12345', 8))  # 转换成int 8进制 转成10进制


# 默认转二进制字符串
def int2(x, base=2):
    return int(x, base)


print(int2('100000'))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2_10()，可以直接使用下面的代码创建一个新的函数int2_10：
int2_10 = functools.partial(int, base=2)
print(int2_10('100000'))

max2 = functools.partial(max, 10)  # 实际上会把10作为*args的一部分自动加到左边

print(max2(5, 6, 7))  # 相当于：args = (10, 5, 6, 7) max(*args)

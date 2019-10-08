# -*- coding: utf-8 -*-
# 返回函数练习 闭包   返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


def lazy_sum(*args):
    def sum():
        rnum = 0
        for n in args:
            rnum = rnum + n
        return rnum

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())

# 闭包 每次都返回一个新的函数 其内部的局部变量还被新函数引用
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2, f1(), f2())


# 产生问题 结果都是9
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


# 如果一定要引用循环变量,就再创建一个函数，用函数的参数绑定循环变量的值
def count1():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count1()
print(f1(), f2(), f3())


# 计数器
def createCounter():
    a = 0

    def counter():
        nonlocal a  # 标志该变量是上一级的局部变量
        a += 1
        return a

    return counter


def createCounter2():
    def plus():
        n = 1
        while True:
            yield n
            n += 1
    x = plus()

    def counter():
        return next(x)

    return counter


# 测试:
counterA = createCounter2()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter2()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

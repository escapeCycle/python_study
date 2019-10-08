#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# _ 和 __ 以及 __xxx__ 的含义 __xxx__ 是特殊变量, _xxx 是private的含义
# python3 module_test1.py TIANH

' a test module '
__author__ = 'tianh'
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello,World!')
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('too many args!')


if __name__ == '__main__':
    test()


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


# 隐藏逻辑部分 , 不让外部直接调用
def greeting(name):
    if (len(name)) > 1:
        return _private_1(name)
    else:
        return _private_2(name)


# print(greeting('tianh'))
# print(greeting('t'))

# -*- coding: utf-8 -*-

#====================
#File: abop.py
#Author: Wendy
#Date: 2013-12-03
#====================

#eclipse pydev, python3.3

#函数
def sayHello():
    print('Hello World')
    
sayHello()
sayHello()

#带参数的函数
def printMax(a, b):
    if a > b:
        print(a, 'is maximum') #python自动生成空格
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

printMax(3, 4)
x = 5
y = 7
printMax(x, y)

#全部变量
num = 50
def func():
    global num #全局变量, 不建议使用
    print('num is', num)
    num = 2
    print('Changed local num to', num)
    
func()
print('x is still', num)

#非局部变量
def func_outer():
    x = 2
    print('x is', x)
    
    def func_inner():
        nonlocal x #非局部变量, 函数内可见
        x = 5
    
    func_inner()
    print('Changed local x to', x)

func_outer()

#默认参数
def say(message, times = 1):
    print(message*times)

say('Caroline')
say('Wendy', 5)

#关键参数, 指定参数
def func(a, b=5, c=10):
    print('a is', a, 'b is', b, 'c is', c)

func(1) #a的值必须要指定
func(2, c=50)
func(c = 100, a=5)

#可变参数, *number是数组, **keywords是字典(map)
def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        print(key) #打印key
        count += keywords[key]
    return count

print(total(10, 4, 5, 6, Caroline = 50, Wendy = 100))

#返回值, 比较大小使用库函数max
def maximum(x, y):
    if x>y:
        return x
    else:
        return y

print(maximum(2, 3))

#表面return None
def someFunction():
    pass

print(someFunction())

#函数文档
#格式: 首行以大写字母开始, 句号结尾, 次行空格, 接下来是描述
def Welcome(x, y):
    '''
    Welcome to Caroline's world. 
    
    Wendy and me will tell you how to write python.
    '''
    print(x)
    print(y)

Welcome('Caroline', 'Wendy')
print(Welcome.__doc__)

help(Welcome) #帮助信息






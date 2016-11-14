# -*- coding: UTF8 -*-

import os

# filename = os.environ.get('PYTHONSTARTUP')
# if filename and os.path.isfile(filename):
#     exec (open(filename).read())
#
# a, b = 0, 1
# while b < 1000:
#     print(b)
#     a, b = b, a+b

# if语句
# x = int(input('negative changed an integer:'))
#
# if x<0:
#     print ('我小于零')
# elif x==0:
#     print ('我等于零')
# elif x==1:
#     print ('我等于一')
# else:
#     print ('我大于一')

# for语句
# a = ['a','b','c','d']
# for x in a:
#     # print(x,len(x))
#     if len(x) > 6: a.insert(0, x)


# for n in range(2,10):
#     for x in range(2,n):
#         if n%x ==0:
#             print (n,'equals',x,'*',n//x)
#             break
#     else:
#             print (n,'is a prime number')

# 函数的定义
# def fib(n):
#     a,b = 0,1
#     while a<n:
#         print(a)
#         a,b = b,a+b
#
#
# f = fib
# f(100)

# def fib2(n):
#     result = []
#     a,b = 0,1
#     while a<n:
#         result.append(a)
#         a,b = b,a+b
#     return result
#
#
# f100 = fib2(100)
# print (f100)


# def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise IOError('refusenik user')
#         print(complaint)
#
# ask_ok('Do you really want to quit?')


#默认值只能被定义一次
# i = 5
# def f(arg=i):
#     print (arg)
#
# i =6
# f()


# 下面的函数在后续调用过程中会累积（前面）传给它的参数:
# def f(a, L=[]):
#     L.append(a)
#     return L
#
# print(f(3))
# print(f(2))
# print(f(1))

a = ['a','b','c','d']
b = []
# a.append('e')
b.extend(a)
b.insert(2,'r')
# b.remove('r')
b.pop(3)
a = b.index('d')
print a
print b

















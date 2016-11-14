# -*- coding: UTF8 -*-
import math


def add(x,y,f):
    return f(x)+f(y)

print add(-6,9,abs)
print add(25,9,math.sqrt)



#函数map()是 Python 内置的高阶函数,
# 它接收一个函数 f 和一个 list，
# 并通过把函数 f 依次作用在 list 的每个元素上，
# 得到一个新的 list 并返回
def format_name(s):
    return s.capitalize()
print map(format_name,['name','LISA','barT'])

def xx(s):
    return s*s
print map(xx,[1,2,3,4,5])


# reduce()函数也是Python内置的一个高阶函数。
# reduce()函数接收的参数和 map()类似，一个函数 f，一个list，
# 但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，
# reduce()对list的每个元素反复调用函数f，并返回最终结果值。

def prod(x,y):
    return x+y
print reduce(prod,[1,2,3,4,5,6],88) #冲88开始从1加到6

def prox(x,y):
    return x*y
print reduce(prox,[2,4,5,7,12],1)

# filter()函数是 Python 内置的另一个有用的高阶函数，
# filter()函数接收一个函数 f 和一个list，
# 这个函数 f 的作用是对每个元素进行判断，返回 True或 False，
# filter()根据判断结果自动过滤掉不符合条件的元素，
# 返回由符合条件元素组成的新list。
def is_sqr(x):
    return math.sqrt(x)%1==0

print filter(is_sqr,range(1,101))

# Python内置的 sorted()函数可对list进行排序：
print (sorted([32,2.45,3,454,342]))

def cmp_ignore_case(s1,s2):
    return cmp(s1.lower(),s2.lower())
print sorted(['b','ere','Wdfd','Ads'],cmp_ignore_case)


# 像这种内层函数引用了外层函数的变量（参数也算变量），
# 然后返回内层函数的情况，称为闭包（Closure）
def count():
    fs = []
    for i in range(1,4):
        def fa(i):
            return lambda :i*i
        fs.append(fa(i))
    return fs
f1,f2,f3 = count()
print (f1())
print (f2())
print (f3())

# 关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。
print filter(lambda s:s and len(s.strip())>0,['test', None, '', 'str', '  ', 'END'])


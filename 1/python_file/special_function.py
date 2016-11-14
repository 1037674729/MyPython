# -*- coding: UTF8 -*-

# 特殊方法的定义
# 如果要把一个类的实例变成 str，就需要实现特殊方法__str__()：
class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return '(Person:%s, %s)'%(self.name,self.gender)

p = Person('小明','女')
print p


class Fib(object):
    def __init__(self,num):
        self.num = num
        self.fibo = [0,1]
        i = 2
        while i<self.num:
            self.fibo.append(self.fibo[i-2]+self.fibo[i-1])
            i = i+1
    def __str__(self):
        return str(self.fibo)

    def __len__(self):
        return len(self.fibo)

f = Fib(10)
print f
print len(f)

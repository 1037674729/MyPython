# -*- coding: UTF8 -*-


# 继承类
class Person(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

class Teacher(Person):
    def __init__(self,name,sex,age):
        super(Teacher, self).__init__(name,sex)
        self.age = age

t = Teacher('steven','男',18)
print t.name
print t.sex
print t.age


# 函数isinstance()可以判断一个变量的类型，
# 既可以用在Python内置的数据类型如str、list、dict，
# 也可以用在我们自定义的类，它们本质上都是数据类型。

class Person1(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
class Teacher1(Person1):
    def __init__(self,name,sex,age):
        super(Teacher1, self).__init__(name,sex)
        self.age = age
class Student1(Teacher1):
    def __init__(self,name,sex,age,grate):
        super(Student1, self).__init__(name,sex,age)
        self.grate = grate

a = Teacher1('stevens',20,'男')
b = Student1('xiaoliuliu',23,'女','三年级二班')
print isinstance(b,Student1)
print a.age
print b.age
print b.grate


import json
class Student2(object):
    def read(self):
        return r'["Tim","Bob","Alice"]'

s = Student2()
print json.load(s)

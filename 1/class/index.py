# -*- coding: UTF8 -*-

class Person:
    def __init__(self,name):
        self.name = name

xiaoming = Person("xiaoming")
xiaohong = Person("xiaohong")
li = [xiaoming,xiaohong]

print xiaoming.name
print xiaohong.name
print xiaohong.name==xiaoming.name



class Person1(object):
    pass
p1 = Person1()
p1.name = 'steven'
p2 = Person1()
p2.name = 'peter'
p3 = Person1()
p3.name = 'kitty'

L = [p1,p2,p3]
L1 = sorted(L,key=lambda x:x.name)
print L1[0].name
print L1[1].name
print L1[2].name


class Person2(object):
    def __init__(self,name,gender,birth):
        self.name = name
        self.gender = gender
        self.birth = birth


xiaoliu = Person2('steven','男','1998-2-23')
print xiaoliu.gender

# 访问限制__XX的形式不能直接被外部访问
class Person3(object):
    def __init__(self,name,score):
        self.name = name
        self.__score = score
        self.scse= self.__score


p = Person3("小明","100")
print p.name
print p.scse

# 创建类的属性
class Person4(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Person4.count = Person4.count+1

p1 = Person4('Bob')
print p1.count

p2 = Person4('steven')
print p2.count

# class Person5(object):
#     __count = 0
#     def __init__(self,name):
#         self.name = name
#         Person5.__count = Person5.__count+1
#
# p1 = Person5('Bob')
# p2 = Person5('Alice')
#
# print Person5.__count


# 定义实例方法
class Person6(object):
    def __init__(self,name,score):
        self.name = name
        self.__score = score
    def get_grade(self):
        scores = self.__score
        if scores>=80:
            return 'A-优秀'
        elif scores>60 and scores<80:
            return 'B-及格'
        elif scores<60:
            return 'C-不及格'

p11 = Person6('小强',50)
p22 = Person6('小强强',100)
print p11.get_grade()
print p22.get_grade()

# 定义类方法
class Person(object):
    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count

    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1


print Person.how_many()

p1 = Person('Bob')

print Person.how_many()
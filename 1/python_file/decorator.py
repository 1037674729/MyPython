# -*- coding: UTF8 -*-

#Python装饰器可以简化代码的重复使用.



# Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。
# 使用 decorator 用Python提供的 @ 语法，这样可以避免手动编写 f = decorate(f) 这样的代码。


#不带参数的定义
# 考察一个@log的定义
def log(f):
    def fn(x):
        print 'call '+ f.__name__+'().....'
        return f(x)
    return fn

@log
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
print factorial(10)

#编写一个时间日志
import time
def performance(f):
    def print_time(*args,**kwargs):
        print 'call '+f.__name__+'() in '+time.strftime('%Y-%m-%d',time.localtime(time.time()))
        return f(*args,**kwargs)
    return print_time

@performance
def factorials(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
print factorials(10)

#带参数的定义
def performa(unit):
    def pix_decorator(f):
        def wrapper(*args,**kwargs):
            t1 = time.time()
            r = f(*args,**kwargs)
            t2 = time.time()
            t = (t2-t1)*1000 if unit=='ms' else (t2-t1)
            print 'call %s() in %f %s'%(f.__name__,t,unit)
            return r
        return wrapper
    return pix_decorator

@performa('ms')
def factor(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
print factor(10)



import time, functools

def performance(unit):
    def fn(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t0 = time.time()
            back = f(*args, **kw)
            t1 = time.time()
            t = (t1 - t0) if unit =='s' else (t1 - t0) * 1000
            print 'call %s() in %s %s' % (f.__name__, t, unit)
            return back
        return wrapper
    return fn

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(3)
print factorial.__name__
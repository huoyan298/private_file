# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
# This is decorator
import time
def logger(func):
    def wrapper(*args,**kwargs):
        print("函数开始执行".format(func.__name__))
        func(*args,**kwargs)
        print("函数计算完了")
    return wrapper

def print_h():
    print("xue xi decorator")
# 这里使用不带括号，不将helloworld为参数传入，有点意外
@logger
def helloworld():
    print("hello world")

@logger
def add(x, y):
  print('{} + {} = {}'.format(x, y, x+y))

# time
def timer(func):
    def wrapper(*args,**kwargs):
        t1=time.time()
        func(*args,**kwargs)
        t2=time.time()
        const_time=t2-t1
        print("时间：{}s".format(const_time))
    return wrapper

@timer
def want_sleep(sleep_time):
    time.sleep(sleep_time)


def american():
    print("I am from america")

def chinese():
    print("I am come from china")

def say_hello(coutry):
    def wrapper(func):
        def deco(*args,**kwargs):
            if coutry== "china":
                print("你好")
            elif coutry=="America":
                print("hello America")
            else:
                return

            func(*args,**kwargs)
        return deco
    return wrapper


@say_hello("china")
def chinese():
    print("我来自中国")

@say_hello("America")
def american():
    print("I am from America")


class logger(object):
    def __init__(self,func):
        self.func =func

    def __call__(self, *args, **kwargs):
        print("[INFO]:the function {func}() is running...".format(func=self.func.__name__))
        return self.func(*args,**kwargs)

@logger
def say(something):
    print("say {}".format(something))


class logg(object):
    def __init__(self,level='INFO'):
        self.level=level

#这里竟然不是 __call__(self,*args,**kwargs)
    def __call__(self, func):
        def wrapper(*args,**kwargs):
            print( "[{level}]: the function {func}() is running..." .format( level=self.level, func=func.__name__ ) )
            func(*args,**kwargs)
        return wrapper

@logg(level="WARNING")
def say(something):
    print("say {}".format(something))


import functools
class DelayFunc:
    def __init__(self,duration,func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} seconds ')
        time.sleep(self.duration)
        return self.func(*args,**kwargs)
# 为啥这里返回的要带参数呢

    def eager_call(self,*args,**kwargs):
        print('Call without delay')
        return self.func(*args,**kwargs)


def delay(duration):
    """
    装饰器":推迟某函数的执行,同时提供eager_call方法立即执行
    """
    return functools.partial(DelayFunc, duration)


@delay(duration=2)
def add(a,b):
    return a+b


#装饰类的装饰器
instances={}

def singleton(cls):
    def get_instance(*args,**kwargs):
        cls_name=cls.__name__
        print('======1=====')
        if not cls_name in instances:
          print('====2====')
          instance=cls(*args,**kwargs)
          instances[cls_name]=instance
        return instances[cls_name]
    return get_instance

@singleton
class User:
    _instance =None
    def __init__(self,name):
        print('====3===')
        self.name = name



# 9.wraps 装饰器有啥用
def wrapper(func):
    def inner_function():
        pass
    return inner_function

@wrapper
def wrapped():
    pass


# 10.
def wrapper(func):
    def inner_function():
        pass
    return inner_function

def wrapped():
    pass

# 11
from functools import wraps
def wrapper(func):
    @wraps(func)
    def inner_function():
        pass
    return inner_function

    @wrapper
    def wrapped():
        pass

''' 12 函数
def wraps(wrapped,
     assigned = WRAPPER_ASSIGNMENTS,
     updated = WRAPPER_UPDATES):
  return partial(update_wrapper, wrapped=wrapped,
          assigned=assigned, updated=updated)

from functools import update_wrapper

WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
            '__annotations__')

def wrapper(func):
  def inner_function():
    pass

  update_wrapper(inner_function, func, assigned=WRAPPER_ASSIGNMENTS)
  return inner_function

@wrapper
def wrapped():
  pass

print(wrapped.__name__)
'''

# 12 property
class Student(object):
    def __init__(self,name,age=None):
        self.name= name
        self.age =age

XM = Student("小明")
XM.age = 23
print('12',XM.age)
del XM.age
XM.age = 22
# 'Student' object has no attribute 'age'
print('del:',XM.age)


'''
import signal

class TimeoutException(Exception):
  def __init__(self, error='Timeout waiting for response from Cloud'):
    Exception.__init__(self, error)


def timeout_limit(timeout_time):
  def wraps(func):
    def handler(signum, frame):
      raise TimeoutException()

    def deco(*args, **kwargs):
      signal.signal(signal.SIGALRM, handler)
      signal.alarm(timeout_time)
      func(*args, **kwargs)
      signal.alarm(0)
    return deco
  return wraps
'''


if __name__=="__main__":
    # helloworld()
    # add(20,50)
    # want_sleep(3)

    # chinese()
    # print("-------")
    # american()

    # say("你好啊")

    # say("hai hello")

    # add   ????????
    # add(7,9)

    # add.func

    '''
    u1=User('wangbm1')
    u1.age =20
    u2=User('wangebm2')
    print(u2.age)
    print( u1 is u2)
    '''
    '''
    # 9.  inner_function
    print("9",wrapped.__name__)

    #10  inner_function
    print("10",wrapper(wrapped).__name__)

    #11 wrapped
    print(wrapped.__name__)
    '''


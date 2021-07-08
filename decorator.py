# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm



#任务超时退出
import functools
from  concurrent import futures
executor = futures.ThreadPoolExecutor(1)
def timeout(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            future =executor.submit(func,*args,**kwargs)
            return future.result(timeout = seconds)
        return wrapper
    return  decorator

#类装饰器
import functools
from concurrent import  futures

class timeout:
  _executor = futures.ThreadPoolExecutor(1)

  def __init__(self,seconds):
      self.seconds = seconds

  def __call__(self, func):
      @functools.wraps(func)
      def wrapper(*args,**kw):
          future = timeout._executor.submit(func,*args,**kw)
          return future.result(timeout=self.seconds)
      return wrapper

# 日志记录

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        import time
        start = time.perf_counter()
        res = func(*args,**kw)
        end = time.perf_counter()
        print(f'函数 { func.__name__} 耗时 {(end -start)*1000} ms')
        return res
    return wrapper

# 缓存
import math
from functools import lru_cache
import random
@lru_cache()
def task(x):
    import time
    time.sleep(0.01)
    return round(math.log(x**3 /15),4)


# 约束某个函数的可执行次数
import functools
class allow_count:
    def __init__(self,count):
        self.count = count
        self.i = 0

    def __call__(self,func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            if self.i >= self.count:
                return
            self.i +=1
            return func(*args,**kw)
        return wrapper

@allow_count(3)
def job(x):
    x+=1
    return x


for i in range(5):
    print(job(i))


if __name__ =="__main__":
    @timeout(1)
    def task(a,b):
        # time.sleep(1.2)
        import time
        time.sleep(0.9)
        return a+b
       #return lambda a,b:a+b

print(task(2,3))
# print(task(2,3)(1,2))

#
@log
def now():
    print("2021-7-1")


now()





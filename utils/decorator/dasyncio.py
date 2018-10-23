# -*- coding: utf-8 -*-
'''
  基于python Threading模块封装的异步函数装饰器
'''
from threading import Thread
import time

'''
async_call为一次简单的异步处理操作，装饰在要异步执行的函数前，再调用该函数即可执行单次异步操作(开辟一条新的线程)
'''
def async_call(fn):
    def wrapper(*args, **kwargs):
        Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper

'''
async_pool为可定义链接数的线程池装饰器，可用于并发执行多次任务
'''
def async_pool(pool_links):
    def wrapper(func):
        def sub_wrapper(*args,**kwargs):
            for x in range(0,pool_links):
                Thread(target=func, args=args, kwargs=kwargs).start()
                #func(*args, **kwargs)
        return sub_wrapper
    return wrapper

'''
async_retry为自动重试类装饰器，不支持单独异步，但可嵌套于 call 和 pool中使用
'''
def async_retry(retry_times,space_time):
        def wrapper(func):
            def sub_wrapper(*args, **kwargs):
                try_times = retry_times
                while try_times > 0:
                    try:
                        func(*args, **kwargs)
                        break
                    except Exception as e:
                        print(e)
                        time.sleep(space_time)
                        try_times = try_times - 1
            return sub_wrapper
        return wrapper

# 以下为测试案例代码
#
# @async_call
# def sleep2andprint():
#     time.sleep(2)
#     print('22222222')
#
# @async_pool(pool_links=5)
# def pools():
#     time.sleep(1)
#     print('hehe')
#
#
# @async_retry(retry_times=3,space_time=1)
# def check():
#     a = 1
#     b ='2'
#     print(a+b)
#
# def check_all():
#     print('正在测试async_call组件')
#     print('111111')
#     sleep2andprint()
#     print('333333')
#     print('若3333出现在22222此前，异步成功')
#     print('正在测试async_pool组件')
#     pools()
#     print('在一秒内打印出5个hehe为成功')
#     print('正在测试async_retry组件')
#     check()
#     print('打印三次异常则成功')
#
# check_all()


# -*- coding: utf-8 -*-
'''
需要多次调试的不稳定性任务，或者需要统计耗时的任务，可以使用下列装饰器
'''

import time

#任务计时器
#任务名
def timer(name):
    def wrapper(func):
        def sub_wrapper(*args,**kwargs):
            ctime = time.time()
            print("接收到一个任务",name)
            func(*args,**kwargs)
            etime = time.time() - ctime
            print("任务耗时",etime)
        return sub_wrapper
    return wrapper


#自动重新执行的任务
#任务名 + 重试次数
def retry_work(name,times):
    def wrapper(func):
        def sub_wrapper(*args,**kwargs):
            try_times = times
            while times>0:
                 try:
                    print("执行任务",name,'次数',try_times)
                    func(*args,**kwargs)
                    print("任务完成")
                    break
                 except Exception as e:
                    print(e)
                    time.sleep(1)
                    try_times=try_times-1
        return sub_wrapper
    return wrapper


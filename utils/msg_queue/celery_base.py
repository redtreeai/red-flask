# -*- coding: utf-8 -*-
# @Time    : 19-12-2 下午3:34
# @Author  : Redtree
# @File    : celery_base.py
# @Desc :  基于celery实现简单的分布式消息分发


from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
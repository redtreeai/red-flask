# -*- coding: utf-8 -*-
# @Time    : 19-12-2 下午3:36
# @Author  : Redtree
# @File    : celery_dojob.py
# @Desc :

from utils.msg_queue.celery_base import add

add.delay(4,4)
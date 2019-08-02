# -*- coding: utf-8 -*-
# @Time    : 19-5-30 上午11:18
# @Author  : Redtree
# @File    : redisor.py
# @Desc : redis操作封装
import redis
from utils.decorator.dasyncio import async_call


def connect_redis():
    # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    return r


@async_call
def update_redis_kv(redis_obj, r_key, r_value):
    try:
        redis_obj.set(r_key, r_value)
        return True
    except Exception as err:
        return False


#redis取值操作
def get_redis_value_by_key(redis_obj, r_key):
    try:
        return redis_obj[r_key]
    except Exception as err:
        return False


#redis删除操作
def delete_redis_key(redis_obj, r_key):
    try:
        redis_obj.delete(r_key)
        return True
    except Exception as err:
        return False
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


#操作5种数据类型的案例
def redis_five_datatype_test():

    print('测试链接数据库')
    rbj = connect_redis()
    print('获取数据库链接')
    print(rbj)
    print('字符串')
    rbj.set("name", "Jack", ex=20)
    rst = rbj.get("name")
    print(rst)
    print('list')
    rbj.lpush("object", 'one')
    rbj.lpush("object", 'two')
    rbj.lpush("object", 'three')
    rbj.lpush("object", 'four')
    rbj.lpush("object", 'five')
    rbj.lpush("object", 'six')
    #return a slice
    ret = rbj.lrange("object", 0, 5)
    print(ret)
    print(ret[::-1])
    print("The length of ret is:", len(ret))
    print('hash')
    rbj.hset("user:info", "name", "Jack")
    rbj.hset("user:info", "age", "20")
    rbj.hset("user:info", "phone", "12345678900")
    rbj.hset("user:info", "email", "2564493603@qq.com")
    rst = rbj.hgetall("user:info")
    print(rst)
    print('集合set')
    rbj.sadd("set", "one")
    rbj.sadd("set", "two")
    rbj.sadd("set", "three")
    res = rbj.smembers("set")
    print(res)
    print('有序结合zet')
    rbj.zadd("mark", "one", 1)
    rbj.zadd("mark", "two", 2)
    rbj.zadd("mark", "three", 3)
    rbj.zadd("mark", "four", 4)
    rbj.zadd("mark", "five", 5)
    res = rbj.zrange("mark", 3, 5)
    print(res)

#redis_five_datatype_test()
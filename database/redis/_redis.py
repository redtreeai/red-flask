# 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
#当redis IO操作较为频繁的时候，应将redis对象在FLask工程中全局初始化。
import redis

def connect_redis():
    # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    return r

def add_kv(redis_obj,r_key,r_value):
    redis_obj.set(r_key, r_value)
    return 'success'

def get_by_key(redis_obj,r_key):
    print(redis_obj[r_key])
    print(redis_obj.get(r_key))  # 取出键name对应的值
    print(type(redis_obj.get(r_key)))
    return 'success'


# -*- coding: utf-8 -*-
# @Time    : 19-12-2 下午2:28
# @Author  : Redtree
# @File    : rmq_send.py
# @Desc : 面向rabbitMQ消息队列的处理案例(生产者)


import pika
import random


'''
使用rabbitMQ需要实现在服务器安装rabbit_server,依赖于erlang环境.详细的安装方式自行搜索。

python依赖中，建议使用librabbitmq,这是官方推荐的基于c++链接的mq库

pip install "celery[librabbitmq,redis,msgpack]"

'''

# 新建连接，rabbitmq安装在本地则hostname为'localhost'
hostname = 'localhost'
parameters = pika.ConnectionParameters(hostname)
connection = pika.BlockingConnection(parameters)

# 创建通道
channel = connection.channel()
# 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
channel.queue_declare(queue='hello')

number = random.randint(1, 1000)
body = 'hello world:%s' % number
# 交换机; 队列名,写明将消息发往哪个队列; 消息内容
# routing_key在使用匿名交换机的时候才需要指定，表示发送到哪个队列
channel.basic_publish(exchange='', routing_key='hello', body=body)
print(" [x] Sent %s" % body)
connection.close()



# -*- coding: utf-8 -*-
# @Time    : 19-12-2 下午3:18
# @Author  : Redtree
# @File    : rmq_recieve.py
# @Desc :面向rabbitMQ消息队列的处理案例(消费者 )


import pika

'''
使用rabbitMQ需要实现在服务器安装rabbit_server,依赖于erlang环境.详细的安装方式自行搜索。
'''

hostname = 'localhost'
parameters = pika.ConnectionParameters(hostname)
connection = pika.BlockingConnection(parameters)

# 创建通道
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print (" [x] Received %r" % (body,))

# 告诉rabbitmq使用callback来接收信息  (旧的版本参数顺序是 callback 'hello'对调)
channel.basic_consume('hello',callback,True)

# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理,按ctrl+c退出
print (' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
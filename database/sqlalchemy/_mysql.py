# -*- coding: utf-8 -*-
'''
基于sqlalchemy模块的orm基础配置,当性能不佳时，建议使用原生sql语句重写核心模块
'''

#调试模式是否开启
DEBUG = False

SQLALCHEMY_TRACK_MODIFICATIONS = False
#session必须要设置key
SECRET_KEY='~XHH!jmN]LWX/,?RTA0Zr98j/3yX R'

#mysql数据库连接信息,这里改为自己的账号  #直连模式启动
HOSTNAME = '127.0.0.1'
PORT = '3310'
DATABASE = 'testdb'
USERNAME = 'root'
PASSWORD = 'root'
#链接模式
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

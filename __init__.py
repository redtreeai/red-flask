# -*- coding: utf-8 -*-
'''
 Flask 初始化配置文件,包含基本配置，ORM，数据缓存，模型预加载，控制器注册等，注意业务逻辑顺序
'''
from flask_cors import CORS  #添加CORS组件 允许跨域访问
from flask import Flask, request,make_response,send_from_directory
import os
import yaml

'''
Flask基础配置部分
'''
print('初始化Flask—APP，加载相关组件')
# 初始化Flask对象
app = Flask(__name__)
# 初始化session 会话  需要配置key
app.secret_key = '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\'
#实例化 cors
CORS(app, supports_credentials=True)
#其他组件注册
request = request
make_response = make_response
send_from_directory = send_from_directory

'''
适应性配置，方便本地调试和部署线上
'''
print('读取适应性配置')
#获取服务器基本配置信息
setting = yaml.load(open('setting.yaml',encoding= 'utf-8'),Loader=yaml.FullLoader)
SERVER_IP = setting['SERVER_IP']
SERVER_PORT = int(setting['SERVER_PORT'])
VERSION = setting['VERSION']
DESCRIPTION = setting['DESCRIPTION']
# 数据库常量配置
PAGE_LIMIT = int(setting['PAGE_LIMIT'])
DEFAULT_PAGE = int(setting['DEFAULT_PAGE'])
USER_SALT_LENGTH = int(setting['USER_SALT_LENGTH'])
#字符串编码格式
STRING_CODE = setting['STRING_CODE']
#加密方式名
ENCRYPTION_SHA1 =setting['ENCRYPTION_SHA1']
#token过期时间配置
TOKEN_EXPIRE = int(setting['TOKEN_EXPIRE'])


#获取部署目录,ROOT_PATH即可作为工程中的绝对路径根目录，方便业务逻辑调用
ROOT_PATH = os.popen('chdir','r',1).read() #linux下使用pwd
ROOT_PATH = str(ROOT_PATH).replace('\n','')

'''
数据库对象的创建和预加载,包含Redis/MongoDB等皆应在此提前实例化，如果需要从resource预先缓存数据，
例如读取txt/csv等文件，也可以在此处预先加载，以供全局调用。
'''
print('连接数据库')
from sqlalchemy import create_engine  #加载配置文件内容
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.sqlalchemy import _mysql  # 连接数据库的数据

engine_mysql = create_engine(_mysql.DB_URI,  pool_pre_ping=True,
    echo=False,
    max_overflow=5,  # 超过连接池大小外最多创建的连接
    pool_size=10,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=3600  # 多久之后对线程池中的线程进行一次连接的回收（重置）
 ) # 创建引擎
Base_mysql = declarative_base(engine_mysql)
DBSession_ams_mysql = sessionmaker(bind=engine_mysql) # sessionmaker生成一个session类 此后DBSession_mysql将可在全局作为一个数据库会话对象持续服务,不用重复创建

print('服务启动成功,版本:'+str(VERSION)+'\n'+'版本描述:'+DESCRIPTION)
'''
所有的控制器在此处注册方可生效
'''
#注册控制器
from controller import apis  #api-demo
from controller.admin import sys_user




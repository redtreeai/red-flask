# -*- coding: utf-8 -*-
'''
 Flask 初始化配置文件,包含基本配置，ORM，数据缓存，模型预加载，控制器注册等，注意业务逻辑顺序
'''

import subprocess
from flask_cors import CORS  # 添加CORS组件 允许跨域访问
from flask import Flask, request, make_response, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_sockets import Sockets
from flask_migrate import Migrate,MigrateCommand
import platform
import config
from flask_script import Manager

'''
Flask基础配置部分
'''
print('初始化Flask—APP，加载相关组件,启动账号管理服务v.01')
# 初始化Flask对象

app = Flask(__name__)
# 初始化session 会话  需要配置key
app.secret_key = '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\'
# 实例化 cors
CORS(app, supports_credentials=True)
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# 子命令  MigrateCommand 包含三个方法 init migrate upgrade
manager = Manager(app)
manager.add_command('db', MigrateCommand)
sockets = Sockets(app)

SYS_ENV = 'Windows'
if(platform.system()=='Windows'):
    SYS_ENV='Windows'
elif(platform.system()=='Linux'):
    SYS_ENV='Linux'
# 其他组件注册
request = request
make_response = make_response
send_from_directory = send_from_directory



'''
适应性配置，方便本地调试和部署线上
'''
print('读取适应性配置')
# 获取服务器基本配置信息

# 获取部署目录,ROOT_PATH即可作为工程中的绝对路径根目录，方便业务逻辑调用 os.popen会导致pyinstaller打包无窗口模式后报错
ROOT_PATH= subprocess.Popen("chdir",shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
ROOT_PATH=str(ROOT_PATH,encoding="utf-8")
ROOT_PATH =str(ROOT_PATH).replace('\n', '')

'''
数据库对象的创建和预加载,包含Redis/MongoDB等皆应在此提前实例化，如果需要从resource预先缓存数据，
例如读取txt/csv等文件，也可以在此处预先加载，以供全局调用。
'''
from database import orms

'''
路由注册
'''
from controller import apis
from controller.admin import sys_user #系统账号相关服务
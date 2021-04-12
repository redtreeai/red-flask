# -*- coding: utf-8 -*-
# @ Time   :  2020/9/8 14:56
# @ Author : Redtree
# @ File :  config.py
# @ Desc :


VERSION = 'V0.1'

'''
database_setting
'''

DIALCT = "mysql"
DRIVER = "pymysql"
USERNAME = "mysql-username"
PASSWORD = "123456"
HOST = "数据库连接地址"
PORT = "数据库服务端口"
DATABASE = "testdb"
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALCT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 30
SQLALCHEMY_POOL_RECYCLE = 3600
SQLALCHEMY_MAX_OVERFLOW = 5
SQLALCHEMY_TRACK_MODIFICATIONS = False
'''
Flask-SQLAlchemy有自己的事件通知系统，该系统在SQLAlchemy之上分层。为此，它跟踪对SQLAlchemy会话的修改。
这会占用额外的资源，因此该选项SQLALCHEMY_TRACK_MODIFICATIONS允许你禁用修改跟踪系统。
当前，该选项默认为True，但将来该默认值将更改为False，从而禁用事件系统。
'''

'''
WEB SETTINT
'''
WEB_IP = 'localhost'
WEB_PORT = '5000'
#字符串编码格式
STRING_CODE = 'utf-8'
#加密方式名
ENCRYPTION_SHA1 = 'sha1'
#token过期时间配置(默认一周 604800/测试的时候5分钟)
TOKEN_EXPIRE = 604800

'''
db-select-habit
'''

USER_SALT_LENGTH = 4
PAGE_LIMIT = 10
DEFAULT_PAGE = 1
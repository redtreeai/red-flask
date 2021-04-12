# -*- coding: utf-8 -*-
# @ Time   :  2020/1/13 15:50
# @ Author : Redtree
# @ File :  sys_user_manager 
# @ Desc : 系统用户管理


import random
import string
import hashlib
from __init__ import db
from config import USER_SALT_LENGTH,PAGE_LIMIT, DEFAULT_PAGE
from sqlalchemy import func,or_
from database.sys_user import Sys_user
from utils.http import responser
import json
import time
from utils.decorator import oauth2_tool


# 获取由4位随机大小写字母、数字组成的salt值
def create_salt():
    salt = ''.join(random.sample(string.ascii_letters + string.digits, USER_SALT_LENGTH))
    return salt

# 获取原始密码+salt的md5值
def md5_password(password,salt):
    trans_str = password+salt
    md = hashlib.md5()
    md.update(trans_str.encode('utf-8'))
    return md.hexdigest()

#用户登录认证（HTTP/LDAP）
def check_login(username,password):

    #先检查用户是否被封禁或删除
    try:
        info = Sys_user.query.filter(Sys_user.username == username).first()
        user_data = json.loads(str(info))
        ud_salt = user_data['salt']
        ud_password =user_data['password']
        ud_nickname = user_data['nickname']
        if not md5_password(password,ud_salt)==ud_password:
             #说明密码错误
             return responser.send(10002)
         #无拦截则登录成功,生成access_token返回给用户,token_key为username
        access_token = oauth2_tool.generate_token(username)
        if access_token==False:
             #属于系统级异常，一般是部署的python环境有问题,正常不会触发
             return responser.send(40001)

        res = {'access_token':access_token,'username':username,'nickname':ud_nickname}
         #异步更新登录日志
        return responser.send(10000,res)

    except Exception as err:
        print(err)
        #账号不存在
        return responser.send(10001)


#用户登录认证（HTTP/LDAP）
def auto_login(username,access_token):

    #先检查用户是否被封禁或删除
    try:
        info = Sys_user.query.filter(Sys_user.username == username).first()
        user_data = json.loads(str(info))
        ud_nickname = user_data['nickname']

        res = {'access_token':access_token,'username':username,'nickname':ud_nickname}
        #异步更新登录日志
        return responser.send(10000,res)

    except Exception as err:
        print(err)
        #账号不存在
        return responser.send(10001)






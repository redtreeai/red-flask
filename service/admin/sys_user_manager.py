# -*- coding: utf-8 -*-
# @ Time   :  2020/1/13 15:50
# @ Author : Redtree
# @ File :  sys_user_manager 
# @ Desc : 系统用户管理


import random
import string
import hashlib
from __init__ import DBSession_ams_mysql,PAGE_LIMIT,USER_SALT_LENGTH
from sqlalchemy import func,or_
from database.sqlalchemy.orm_models.sys_user import Sys_user
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
    # 获取会话对象
    session = DBSession_ams_mysql()

    #先检查用户是否被封禁或删除
    try:
        info = session.query(Sys_user).filter(Sys_user.username == username, Sys_user.del_flag == 0).one()
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
        session.close()
        #账号不存在
        return responser.send(10001)


#用户登录认证（HTTP/LDAP）
def auto_login(username,access_token):
    # 获取会话对象
    session = DBSession_ams_mysql()

    #先检查用户是否被封禁或删除
    try:
        info = session.query(Sys_user).filter(Sys_user.username == username, Sys_user.del_flag == 0).one()
        user_data = json.loads(str(info))
        ud_role_code = user_data['role_code']
        ud_role_name = user_data['role_name']
        ud_nickname = user_data['nickname']

        res = {'access_token':access_token,'username':username,'nickname':ud_nickname}
        #异步更新登录日志
        return responser.send(10000,res)

    except Exception as err:
        print(err)
        session.close()
        #账号不存在
        return responser.send(10001)


#查询用户列表
def get_sys_users(page=1,page_size=PAGE_LIMIT):
    try:
        FILTER = (Sys_user.del_flag==0)
        session = DBSession_ams_mysql()
        all_len = session.query(func.count(Sys_user.mp_id)).filter(FILTER).scalar()
        DB_data = session.query(Sys_user).filter(FILTER).order_by(
            Sys_user.update_time.desc()).limit(page_size).offset((int(page) - 1) * page_size).all()

        if not DB_data == 0 and not DB_data == '':
            # print(DB_data)
            DB_data = json.loads(str(DB_data))  # 需要强转字符串才能序列化
            res = {"total": all_len, "data": DB_data}
            session.close()
            return responser.send(10000, res)
        else:
            return responser.send(40002)
    except Exception as err:
        print(err)
        return responser.send(40002)

#新增用户
def add_sys_user(username,password,nickname):

    # 先检查用户是否被封禁或删除
    session = DBSession_ams_mysql()
    try:
        info = session.query(Sys_user).filter(Sys_user.username == username).one()
        session.close()
        return responser.send(10006)
    except Exception as err:
        pass
    # 创建普通HTTP用户
    ctime = int(time.time())
    try:
        salt = create_salt()  # 盐值
        db_password = md5_password(password, salt)  # 入库密码
        info = session.add(
            Sys_user(username=str(username), salt=str(salt), password=str(db_password),nickname=str(nickname),
                        del_flag=0,created_time=int(ctime), updated_time=int(ctime)))
        if not info == 0 and not info == '':
            session.commit()
            session.close()
            return responser.send(10000,'新增HTTP用户:'+str(username)+'成功')
    except Exception as err:
        print(err)
        session.rollback()  # 回滚
        session.close()
        return responser.send(40002)


#删除用户(HTTP/LDAP)
def delete_sys_user(username):
    try:
        session = DBSession_ams_mysql()
        try:
            #暂时未做关联删除
            info = session.query(Sys_user).filter(Sys_user.username==username).delete(
                synchronize_session=False)
            if info >= 0:
                session.commit()
                session.close()
                return responser.send(10000, 'success')
            else:
                session.close()
                return responser.send(40002)
        except:
            session.close()
            return responser.send(40002)
    except:
        return responser.send(40002)


#重置指定用户密码(HTTP/LDAP)
def update_user_pwd(username,password):
    session = DBSession_ams_mysql()
    ctime = int(time.time())
    salt = create_salt()  # 盐值
    db_password = md5_password(password, salt)  # 入库密码
    try:
        info2 = session.query(Sys_user).filter(Sys_user.username == username).update(
            {Sys_user.password:db_password, Sys_user.update_time: ctime})
        if not info2 == 0 and not info2 == '':
            session.commit()
            session.close()
            return responser.send(10000,"用户："+username+'密码重置成功')
    except Exception as err:
        session.close()
        print(err)
        return responser.send(10021)




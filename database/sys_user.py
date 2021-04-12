# -*- coding: utf-8 -*-
# @Time    : 18-8-8 下午3:43
# @Author  : Redtree
# @File    : sys_user.py
# @Desc : 系统用户表orm构造(只是个模板)


from __init__ import db
import json


# 定义好一些属性，与user表中的字段进行映射，并且这个属性要属于某个类型
class Sys_user(db.Model):
    __tablename__ = 'sys_user'

    uuid = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)  # id 整型，主键，自增，唯一
    username = db.Column(db.String(50),comment='账号')
    nickname = db.Column(db.String(50),comment='昵称')
    salt = db.Column(db.String(16),comment='密码盐')
    password=db.Column(db.String(32),comment='入库密码')
    del_flag= db.Column(db.Integer,comment='')
    created_time=db.Column(db.Integer,comment='')
    updated_time=db.Column(db.Integer,comment='')
    created_user = db.Column(db.String(50),comment='')

    def __init__(self, uuid, username, nickname, salt, password, del_flag, created_time, updated_time, created_user):
        self.uuid = uuid
        self.username = username
        self.nickname = nickname
        self.salt = salt
        self.password = password
        self.del_flag = del_flag
        self.created_time = created_time
        self.updated_time = updated_time
        self.created_user = created_user

    def __repr__(self):
        obj = {
            "uuid": self.uuid,
            "username": self.username,
            "nickname": self.nickname,
            "salt": self.salt,
            "password": self.password,
            "del_flag": self.del_flag,
            "created_time": self.created_time,
            "updated_time": self.updated_time,
            "created_user": self.created_user
        }
        return json.dumps(obj)



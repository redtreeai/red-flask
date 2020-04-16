# -*- coding: utf-8 -*-
# @Time    : 18-8-8 下午3:43
# @Author  : Redtree
# @File    : sys_user.py
# @Desc : 系统用户表orm构造(只是个模板)


import json
from __init__ import Base_mysql
from sqlalchemy import (Column, String, Integer)

# 定义好一些属性，与user表中的字段进行映射，并且这个属性要属于某个类型
class Sys_user(Base_mysql):
    __tablename__ = 'sys_user'

    uuid = Column(Integer, primary_key=True)
    username = Column(String(50))
    nickname = Column(String(50))
    salt = Column(String(16))
    password=Column(String(32))
    del_flag= Column(Integer)
    created_time=Column(Integer)
    updated_time=Column(Integer)
    created_user = Column(String(50))

    def __repr__(self):
        get_data = {"uuid":self.uuid, "username":self.username, "nickname":self.nickname, "salt":self.salt,
                    "password":self.password, "del_flag":self.del_flag, "created_time":self.created_time, "updated_time":self.updated_time,"created_user":self.created_user
                  }
        get_data = json.dumps(get_data)
        return get_data
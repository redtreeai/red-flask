# -*- coding: utf-8 -*-
# @Time    : 18-8-8 下午3:43
# @Author  : Redtree
# @File    : sys_user.py
# @Desc : 实验平台系统用户表


import json
from __init__ import Base_mysql
from sqlalchemy import (Column, String, Integer)

# 定义好一些属性，与user表中的字段进行映射，并且这个属性要属于某个类型
class Sys_user(Base_mysql):
    __tablename__ = 'sys_user'

    xid = Column(Integer, primary_key=True)
    userid = Column(String(50))
    nickname = Column(String(50))
    salt = Column(String(16))
    password=Column(String(32))
    del_flag= Column(Integer)
    create_time=Column(Integer)
    update_time=Column(Integer)
    role = Column(String(50))
    create_user = Column(String(50))
    ban_flag = Column(Integer)

    def __repr__(self):
        get_data = {"id":self.id, "userid":self.userid, "nickname":self.nickname, "salt":self.salt,
                    "password":self.password, "del_flag":self.del_flag, "create_time":self.create_time, "update_time":self.update_time,"role":self.role,"create_user":self.create_user
                    ,"ban_flag":self.ban_flag}
        get_data = json.dumps(get_data)
        return get_data
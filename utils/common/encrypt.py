# -*- coding: utf-8 -*-
'''
此工具提供了一个常用的用户密码加密方案，基于md5和随机盐值.
'''
import random
import string
import hashlib

# 获取由4位随机大小写字母、数字组成的salt值
def create_salt():
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    return salt

# 获取原始密码+salt的md5值
def md5_password(password,salt):
    trans_str = password+salt
    md = hashlib.md5()
    md.update(trans_str.encode('utf-8'))
    return md.hexdigest()
# -*- coding: utf-8 -*-
# @Time    : 18-12-7 上午9:50
# @Author  : Redtree
# @File    : regex_matcher.py
# @Desc : 正则匹配工具

import re
#匹配电话号码
def match_phone_number(phone_number):
    phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
    res = re.search(phone_pat, phone_number)
    if res:
        return True
    else:
        return False
#匹配邮箱地址
def match_email(email):
    res =  re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email)
    if res:
        return True
    else:
        return False

#匹配用户id 英文+数字组合
def match_user_id(user_id):
    if re.match('[a-zA-Z0-9]+', user_id) and len(user_id)<=20:
            return True
    else:
            return False


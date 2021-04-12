# -*- coding: utf-8 -*-
# @ Time   :  2021/4/12 14:59
# @ Author : Redtree
# @ File :  sys_user 
# @ Desc :


import requests
import json

def check_login(username,password):
    url = 'http://localhost:5000/login'
    rd = {
        'username':username,
        'password':password
    }
    rd=json.dumps(rd)
    res = requests.post(url,data=rd).text
    return res

'''
账号登录
'''
# res = check_login('admin','admin123')

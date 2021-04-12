# -*- coding: utf-8 -*-
# @ Time   :  2020/4/16 10:55
# @ Author : Redtree
# @ File :  sys_user 
# @ Desc :


from __init__ import app
from __init__ import request
from service.admin import sys_user_manager
from utils.http import responser
from utils.decorator.oauth2_tool import oauth2_check


@app.route('/login', endpoint='login', methods=['POST'])
def check_login():
    '''
    username string 用户名
    password string 密码
    '''
    res_status, rjson = responser.post_param_check(request, ['username', 'password'])
    if res_status == 'success':
        return sys_user_manager.check_login(rjson['username'], rjson['password'])
    else:
        return rjson


@app.route('/auto_login', endpoint='auto_login', methods=['POST'])
@oauth2_check
def auto_login():
    '''
    action_username 执行用户
    access_token 认证令牌
    '''
    res_status, rjson = responser.post_param_check(request, ['action_username', 'access_token'])
    if res_status == 'success':
        return sys_user_manager.auto_login(rjson['action_username'], rjson['access_token'])
    else:
        return rjson




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


@app.route('/get_sys_users', endpoint='get_sys_users', methods=['POST'])
@oauth2_check
def get_sys_users():
    '''
    action_username 执行用户
    access_token 认证令牌
    page  页码，默认为1
    page_size 页宽

    本接口会自动校验用户的授权方式
    '''
    res_status, rjson = responser.post_param_check(request, ['action_username', 'access_token', 'page', 'page_size'])
    if res_status == 'success':
        return sys_user_manager.get_sys_users(rjson['page'], rjson['page_size'])
    else:
        return rjson


@app.route('/add_sys_user', endpoint='add_sys_user', methods=['POST'])
@oauth2_check
def add_sys_user():
    '''
    action_username 执行用户
    access_token 认证令牌
    username  用户账号
    password  用户密码
    nickname  用户昵称
    '''
    res_status, rjson = responser.post_param_check(request, ['action_username', 'access_token'
        , 'username', 'password', 'nickname'])
    if res_status == 'success':
        return sys_user_manager.add_sys_user(rjson['username'], rjson['password'], rjson['nickname'] )
    else:
        return rjson


@app.route('/delete_sys_user', endpoint='delete_sys_user', methods=['POST'])
@oauth2_check
def delete_sys_user():
    '''
    action_username 执行用户
    access_token 认证令牌
    username  待删除用户账号
    '''
    res_status, rjson = responser.post_param_check(request, [ 'action_username', 'access_token','username'])
    if res_status == 'success':
        return sys_user_manager.delete_sys_user(rjson['username'])
    else:
        return rjson


@app.route('/update_user_pwd', endpoint='update_user_pwd', methods=['POST'])
@oauth2_check
def update_user_pwd():
    '''
    action_username 执行用户
    access_token 认证令牌
    username  待更新用户账号
    password 重置密码信息
    '''
    res_status, rjson = responser.post_param_check(request, ['action_username', 'access_token',
                                                          'username', 'password'])
    if res_status == 'success':
        return sys_user_manager.update_user_pwd(rjson['username'], rjson['password'])
    else:
        return rjson

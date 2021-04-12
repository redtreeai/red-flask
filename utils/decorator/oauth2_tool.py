# -*- coding: utf-8 -*-
# @ Time   :  2020/1/14 9:31
# @ Author : Redtree
# @ File :  oauth2_tool 
# @ Desc : Oauth2认证工具


import time
import base64
import hmac
from __init__ import request
from utils.http import responser
from config import TOKEN_EXPIRE
import json


#生成token
def generate_token(key):
    r'''
        @Args:
            key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
            expire: int(最大有效时间，单位为s)
        @Return:
            state: str
    '''
    try:
        ts_str = str(time.time() + int(TOKEN_EXPIRE))
        ts_byte = ts_str.encode("utf-8")
        sha1_tshexstr  = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest()
        token = ts_str+':'+sha1_tshexstr
        b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
        return b64_token.decode("utf-8")
    except:
        return False

#token校验
def certify_token(key, token):
    r'''
        @Args:
            key: str
            token: str
        @Returns:
            boolean
    '''
    try:
        token_str = base64.urlsafe_b64decode(token).decode('utf-8')
        token_list = token_str.split(':')
        if len(token_list) != 2:
            return False
        ts_str = token_list[0]
        if float(ts_str) < time.time():
            # token expired
            return False
        known_sha1_tsstr = token_list[1]
        sha1 = hmac.new(key.encode("utf-8"), ts_str.encode('utf-8'), 'sha1')
        calc_sha1_tsstr = sha1.hexdigest()
        if calc_sha1_tsstr != known_sha1_tsstr:
            # token certification failed
            return False
        # token certification success
        return True
    except:
        return False



def request2json(request):
    return json.loads(request.data)


#Oauth2认证装饰器
def oauth2_check(func):
    def inner(*args,**kwargs):
        try:
            if request.method=='GET':
                rjson = request.args.to_dict()
                key = rjson['action_username']
                token = rjson['access_token']
                if certify_token(key, token) == True:
                    #认证通过则不拦截
                    pass
                else:
                    return responser.send(20001)
            elif request.method=='POST':
                rjson = request2json(request)
                key = rjson['action_username']
                token = rjson['access_token']
                if certify_token(key, token) == True:
                    # 认证通过则不拦截
                    pass
                else:
                    return responser.send(20001)
            else:
                #暂不支持验证其他请求
                return responser.send(30001)
        except Exception as e :
            print('Oauth2认证失败:'+str(e))
            return responser.send(30001)
        return func(*args,**kwargs)
    return inner



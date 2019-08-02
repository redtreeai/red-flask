# -*- coding: utf-8 -*-
# @Time    : 18-10-30 上午9:56
# @Author  : Redtree
# @File    : responser.py
# @Desc :  http请求响应数据封装

import json

CODE = {
    # 正常操作
    10000: '操作成功',

    # 逻辑异常
    10001: '用户不存在',
    10002: '帐号或密码错误',
    10003:'该帐号已被封禁',
    10004:'该角色已被封禁',
    10005:'包含不可操作用户',
    10006:'该记录已存在',
    10007:'机构封禁',
    10008:'邮箱格式错误',
    10009:'电话格式错误',
    10010:'已启用虚拟设备中',
    # http异常
    20001: 'token超时',
    20002: 'ssl证书异常',
    20003: 'JSON格式异常',
    20004: '服务端链接超时',
    20005:'COS服务异常',
    # 非法行为
    30001: '操作非法',
    30002: 'IP黑名单',
    30003: '访问过于频繁',
    30004: '创建帐号含非法角色',
    30005: '填入数据非法',
    30006: '机构类型非法',
    30007: '非法获取授权资源',
    # 系统异常
    40001: '系统异常',
    40002: 'mysql服务异常',
    40003: 'redis服务异常',
    40004: '模型文件丢失',
    40005: 'FFmpeg异常',
    40006: 'shell功能异常',
    # 接口服务
    50001: '接口鉴权失败',
    50002: '参数名错误',
    50003: '文件格式异常',
    50004: '数据长度溢出',
    50005: '转码失败',
    50006: '文件上传失败',
    50007: '数据格式异常',
}


# 返回数据封装
def send(code, data=''):
    if code == 10000 or code == 50002 or code == 10010:
        return json.dumps({'code': code, 'msg': CODE[code], 'data': data})
    else:
        return json.dumps({'code': code, 'msg': CODE[code]})


# request.data 转json
def request2json(request):
    return json.loads(request.data)


def get_param_check(request, param_list):
    try:
        rjson = request.args.to_dict()
        rkeys_list = list(rjson.keys())
        no_match_list = list(set(rkeys_list) ^ set(param_list))
        if len(no_match_list) == 0:
            return 'success', rjson
        else:
            return 'error', send(50002, no_match_list)
    except Exception as e:
        return 'error', send(20003)


# 校验post_json 数据格式是否符合参数列表 若不符合，提示差集
def post_param_check(request,param_list):
    try:
        rjson= request2json(request)
        rkeys_list = list(rjson.keys())
        no_match_list = list(set(rkeys_list) ^ set(param_list))
        if len(no_match_list) == 0:
            return 'success', rjson
        else:
            return 'error', send(50002, no_match_list)
    except Exception as e:
        return 'error', send(20003)




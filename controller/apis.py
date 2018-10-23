# -*- coding: utf-8 -*-
'''
flask作为restful服务时，常用的一些接口类型
'''
from __init__ import app
from __init__ import request,send_from_directory
import json
from utils.decorator.token_maneger import auth_check

#最简单的接口
@app.route('/',methods=['GET'])
def welcome():
   return 'Hello World'

#GET方式传递参数
@app.route('/api/get',methods=['GET'])
def get1():
   page = request.args.get('page')
   return 'this is page'+str(page)

#POST方式传递参数
@app.route('/api/post',methods=['POST'])
def post1():
   # request.json 只能够接受方法为POST、Body为raw，header 内容为 application/json类型的数据
   # json.loads(request.dada) 能够同时接受方法为POST、Body为 raw类型的 Text
   username = request.json('username')
   password = json.loads(request.data)['password']
   if username=='admin' and password == 'admin':
      res = {'code':200,'msg':'suceess','data':username}
      return json.dumps(res)
   res = {'code': 401, 'msg': 'error'}
   return json.dumps(res)

#POST方式传递文件流
@app.route('/api/uploadfile',methods=['POST'])
def uploadfile():
   try:
      f = request.files['file']
      #f.save('path')
      # 获取文件名
      fname = request.form.get("fname")
      res = {'code': 200, 'msg': 'suceess', 'fname': fname}
      return json.dumps(res)
   except Exception as err:
      print(err)
      res = {'code': 401, 'msg': 'error'}
      return json.dumps(res)

#提供下载
@app.route('/api/download',methods=['GET'])
def download():
   return send_from_directory('/directory', 'file', as_attachment=True)

#当使用auth_check装饰时，接口就需要通过token校验。可用来实现登录状态控制等功能,
# 另外,当工程中含有多个auth_check装饰的接口时，需要添加不同的节点命名

@app.route('/api/get1',endpoint='getn1' ,methods=['GET'])
@auth_check
def get1a():
   page = request.args.get('page')
   return 'this is page'+str(page)

@app.route('/api/get2',endpoint='getn2' ,methods=['GET'])
@auth_check
def get2a():
   page = request.args.get('page')
   return 'this is page'+str(page)
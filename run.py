# -*- coding: utf-8 -*-
# @File  : run.py
# @Author: redtree
# @Date  : 18-6-27
# @Desc  :  服务启动入口，自动化判断部署环境并配置UWSGI代理，

from __init__ import app
from __init__ import SERVER_IP
from __init__ import SERVER_PORT
from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop

if SERVER_IP=='localhost':
    #本地调试
    app.run(host='0.0.0.0', port=SERVER_PORT, debug=True, threaded=True)
    #app.run()
     # ssl_context = (
     #    './server.crt',
     #    './server_nopwd.key')
else:
    '''
    windows环境下采用 tornado 充当生产环境的wsgi代理，配合nginx使用。 此处的tornado并不能实现异步无阻塞。
    '''
    # s = HTTPServer(WSGIContainer(app))
    # s.listen(SERVER_PORT)  # 监听 5000 端口
    # print('environment:product wsgi:tornado port:'+str(SERVER_PORT))
    # IOLoop.current().start()

    '''
    Linux环境下使用gunicorn作为生产环境server
    '''
    from werkzeug.contrib.fixers import ProxyFix

    #线上服务部署  对接gunicorn
    app.wsgi_app = ProxyFix(app.wsgi_app)
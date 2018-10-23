# -*- coding: utf-8 -*-
# @File  : run.py
# @Author: redtree
# @Date  : 18-6-27
# @Desc  :  服务启动入口，自动化判断部署环境并配置UWGI代理，

from __init__ import app
from __init__ import SERVER_IP

if SERVER_IP=='localhost':
    #本地调试
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    #app.run()
     # ssl_context = (
     #    './server.crt',
     #    './server_nopwd.key')
else:
    from werkzeug.contrib.fixers import ProxyFix

    # 线上服务部署  对接gunicorn
    app.wsgi_app = ProxyFix(app.wsgi_app)

#简介
深入学习Flask作为RestFul服务端的架构思路。了解Flask设计哲学、应用场景。包含从开发环境搭建、项目架构到生产环境部署的完整教学。 

#目录

1 Flask简介
2 为什么选择Flask
3 开发环境搭建
4 快速构建应用
5 无蓝本路由分离式架构
6 关于数据预加载和内存消耗
7 数据库的开放性选择
8 加密、验证等基础模块的实现
9 节点映射和装饰器的使用
10 并发处理及网络模型的选择
11 服务端部署方案详解

#一、 Flask简介

Flask是一个使用python编写的轻量级web框架，诞生于2010年，作者是Armin Ronacher。Flask的核心部分是Werkzeug和Jinja2。Werkzeug是由Flask作者自己编写的一个基于python WSGI协议的网络服务包。在最初完成werkzeug的时候，Armin Ronacher曾向Bottle(python另一个著名的web框架)的作者推荐使用自己的werkzeug,然而因为设计理念的不同的遭到了拒绝，于是AR亲自操刀上阵，完成了这个github上人气最高的python web框架（目前star数量已超越django）。有趣的是，Flask和Bottle这两个名字都有瓶子的意思。

#二、 为什么选择Flask

Flask最初的设计目的是面向需求简单的小应用，比如博客、公司官网、小论坛等。Flask本身相当于一个提供web基础服务(路由分发、http协议解析、html模板渲染)的内核,其他几乎所有功能都需要依赖于第三方的拓展来实现。相对于django这个全覆盖式服务框架，Flask对于入门pythonWeb开发的新手来说会更难应用。很多人学习Flask时都会被一开始构建第一个helloworld应用时的快速简洁所迷惑，认为flask极其简单，以至于到了之后需要拓展一个flask的业务功能时，却因为无法将其完善成一个django式的通用项目结构和放弃。Flask社区虽然后续推出了Flask-Mail、Flask-Login等模块，但依然鼓励开发者通过Flask-extension的机制去自己造轮子或者选择更适合业务场景的模块。

得益于Flask的设计哲学，其超高的拓展性更加适合未来的程序设计风格。如今人工智能、大数据、云计算等新概念全面普及，软件的需求不再是传统的增删改查，Flask作为云服务的后端时，能够被自由改造成不同形态的项目结构，嵌入各类自定义模块。不论是数据库、数据加密、权限校验、网络模式、前端模板，都可以融入到Flask的体系之中。

需要特别一提的是，Flask默认仅绑定jinja2模板渲染模块，但由于Flask现在更倾向于作为前后端分离工程的后端，所以理论上来说，前端选择vue、react、bootstrap等框架都是支持的。

如果您已经通过学习Flask并能够搭建自己的一套完整的业务框架体系，那么后续的开发效率也将大幅度提升，因为基于python语言的特性和Flask的模块设计，你可以使用比其他框架少很多的篇幅、代码量完成一个常规项目。

所以，我推荐如下几种条件的人可以深入学习并应用Flask:
1 对任意传统web框架有一定了解，比如django,springboot,rails等。
2 软件开发的业务需求多变，趋于易耦合。
3 追求高自由度的开发模式。
4 单纯对这个新兴框架感兴趣。
5 敏捷开发式团队

#三、 开发环境搭建
由于基于WSGI的server基本上依赖于Linux环境，所以建议开发者使用ubuntu或者centos进行开发和部署。以下教程将以ubuntu为例子：

1 通过Anaconda配置Python开发环境,前往https://www.anaconda.com/download/#linux 下载最新的python发布版本。下载完成后是一个shell文件，直接shell anaconda.sh 执行即可。如果有权限问题，先执行 chmod +x. 期间所有配置选择默认的就行。
    
2 修改~/.basrhc,在文件最下方添加

    export PYTHON_HOME=/home/your_user_rootpath/anaconda3
    export PATH=${PYTHON_HOME}/bin

终端输入命令使新环境变量生效

     source ~/.basrhc 

3 在终端输入python，如果有版本提示即是安装成功。

    python
    Python 3.6.5 |Anaconda, Inc.| (default, Apr 29 2018, 16:14:56) 
    [GCC 7.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

#四、 快速构建应用
如果你对完全未接触过Flask,建议先跟着官方文档敲下案例。
Flask官方网站:https://palletsprojects.com/p/flask/
中文版文档:https://dormousehole.readthedocs.io/en/latest/

在掌握Flask各个基础模块的使用后，我们再对Flask的工程结构进行梳理。不难发现，Flask最初的设计是趋向于构建一个单文件应用的，但在实际开发中，将代码分割到多个文件进行管理则更为合理。在不加入蓝图(flask官方的一个拓展模块)的情况下,较难实现分离式项目结构。

如果选择加入blueprint来构建你的Flask项目，那么参照官方文档的说明即可。blueprint本质上是通过注册一个全局__name__参数并绑定相应的路由和模板，然后通过内置钩子函数在Flask应用生成前注册到全局视图层之中。由于是静态配置，一旦载入后，蓝图将不支持拔插，也就是说注册蓝图生成的资源目录和组件都会随着Flask应用的启动而一直存在，不管你是否去调用。

由于本教程针对的是构建restful服务,Flask仅作为提供api的服务，而不执行模板渲染的任务，也就是说不会涉及到视图层的管理，所以我提供了一种新设计方案，并将模板工程上传到了github,同时将快速构建工具上传到了pip官方源。

工程源码:https://github.com/redtreeai/red-flask
快速构建工具:redflask

在配置有python标准开发环境的机器上，通过终端输入命令来快速构建一个red-flask工程。

    pip install redflask==0.1.5
    redflask -b [your_project_name]

基于这个示范工程，我会讲解一种较容易上手的Flask企业项目基础架构方案。

#五、  无蓝本路由分离式架构 

如果你已经构建了一个redflask工程,并且通过IDE工具(推荐使用pycharm/vscode)打开,你会看到工程结果，如下图:

![redflask](https://redtreeblog-1253690989.cos.ap-guangzhou.myqcloud.com/flask/1.png)

通过工程的readme文件我们看到整体的架构说明如下：

    一个基于Flask搭建的Restful_Api服务框架,实现了路由分离的功能但无需依赖于Flask的蓝本。提供了常用的http请求类型和文件传输类型的相关接口。提供了较简单的异步任务分发方案。提供了最常用的用户密码校验模块和token验证模块。集成了Gunicorn+Gevent的服务器自动配置方案。数据库端使用Sqlalchemy和Redis。提供了Flask作为Https服务的解决方案。解决了Flask跨域问题。
    
    #### 使用说明

    1. 本地调试，直接python run.py (请在setting.yaml中配置IP为localhost)
    2. 部署调试，chmod +x test.sh  然后 ./test.sh
    3. 部署生产, chmod +x start.sh 然后 ./start.sh
    
    #### 软件架构
    
    controller : 路由控制器，用来注解并分配工程的api地址和分发对应的接口任务，其作用类似于Java SpringBoot中的restcontroller。子下的文件目录根据对应业务类型进行区分。
    database: 包含各类数据库链接和对象映射的基本配置，以及数据库其他模式（如主从、池化、分布式等）的配置都在此处生效。
    Exceptions: 用来自定义继承或重写python的错误类型，并编写特定的处理方式。
    Resource: 用于存放工程中使用到的各类静态文本数据和多媒体数据，还有机器学习模型。
    Service: 用于编写API实际业务逻辑的文件目录，Controller下的api接口一般会从此处调用具体服务，其目录结构与controller相似。
    Utils: 泛用工具类及全局装饰器的存储目录。
    其他工程文件详解:
    test_case 测试案例写在这里
    __init__.py  red_flask工程的基本配置文件，各项配置须在此初始化
    requirements.txt  记录依赖模块 方便pip安装
    run.py  服务启动入口，wsgi配置文件
    start.sh  服务启动脚本
    test.sh 测试脚本
    configm.py  Gunicorn网络模型配置脚本
    setting.yaml  用于自适应部署的配置文件
    
本章我们先重点讲解__init__.py，controller/apis.py这两个文件。前者这是整个flask工程的初始化配置文件，后者是flask实现路由分离后接口控制器的标准形式文件。

__init__.py(markdown语法问题，此处省略下划线)

    # -*- coding: utf-8 -*-
    '''
     Flask 初始化配置文件,包含基本配置，ORM，数据缓存，模型预加载，控制器注册等，注意业务逻辑顺序
    '''
    from flask_cors import CORS  #添加CORS组件 允许跨域访问
    from flask import Flask, request,make_response,send_from_directory
    import os
    import yaml
    
    '''
    Flask基础配置部分
    '''
    # 初始化Flask对象
    app = Flask(__name__)
    # 初始化session 会话  需要配置key
    app.secret_key = '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\'
    #实例化 cors
    CORS(app, supports_credentials=True)
    #其他组件注册
    request = request
    make_response = make_response
    send_from_directory = send_from_directory
    
    '''
    适应性配置，方便本地调试和部署线上
    '''
    #获取服务器基本配置信息
    setting = yaml.load(open('setting.yaml'))
    SERVER_IP = setting['SERVER_IP']
    
    #获取部署目录,ROOT_PATH即可作为工程中的绝对路径根目录，方便业务逻辑调用
    ROOT_PATH = os.popen('pwd','r',1).read()
    ROOT_PATH = str(ROOT_PATH).replace('\n','')
    
    '''
    数据库对象的创建和预加载,包含Redis/MongoDB等皆应在此提前实例化，如果需要从resource预先缓存数据，
    例如读取txt/csv等文件，也可以在此处预先加载，以供全局调用。
    '''
    
    # from sqlalchemy import create_engine  #加载配置文件内容
    # from sqlalchemy.ext.declarative import declarative_base
    # from sqlalchemy.orm import sessionmaker
    #
    # from database.sqlalchemy import _mysql  # 连接数据库的数据
    #
    # engine_mysql = create_engine(_mysql.DB_URI, echo=False, pool_recycle=3600) # 创建引擎
    # Base_mysql = declarative_base(engine_mysql)
    # DBSession_mysql = sessionmaker(bind=engine_mysql) # sessionmaker生成一个session类 此后DBSession_mysql将可在全局作为一个数据库会话对象持续服务,不用重复创建
    #
    
    '''
    所有的控制器在此处注册方可生效
    '''
    #注册控制器
    from controller import apis

可以看到,该Flask应用的实例化过程遵循一个基本原则，先声明并实例化基本库，然后载入第三方插件或数据集，最后再将接口控制器进行注册生效。这样的设计方式可以让Flask在服务启动前预载入一些会在后期被频繁调用的对象函数或数据到内存中，实现复用效果，而不用频繁重新实例化。另外控制器能在文件底部进行一个集成管理，免去了繁琐的蓝本注册方案。无需在路由文件和初始文件中配置注册蓝本即可实现路由分离的功能。原理相当于是通过python的path管理将Flask工程重新打包成一个单文件应用。

apis.py

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
       
apis.py文件提供了Flask工程在路由分离结构下，控制器文件的标准写法。并提供了部分常用功能的接口范例。从文件中我们可以看到,apis.py先从__init__.py中引入了实例化的Flask应用和基础模块对象，同时，引入了python系统模块组的json库和utils目录下用户自定义的第三方工具类，再去执行接口相关的业务逻辑。从设计角度上来说，控制器尽量只负责为service层（业务逻辑层）转发用户上报到接口的数据并返回处理结果，而不直接在控制器中执行业务逻辑。比如我们在控制器中编写了一个校验用户登录信息的接口，那么实际上他只需要把用户的帐号密码传递给来自service目录下对应的服务文件就行了，然后返回service文件对应函数的处理结果。

在实际的业务场景中，controller目录下建议再进行多级目录分类，然后再根据需求注册到主文件中。那么，在实现路由分离的场景下，整个系统的基础还少了哪个部分呢？没错，就是server的启动了，由于python的web_server大都遵循wsgi协议，所以我们把flask工程的启动部分也单独分离出来编写，以便整合调试不同的网络模型。在redflask工程中，由run.py和configm.py这两个文件来控制工程的调试和部署。

run.py

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
        
由于flask在作为本地调试服务时，采用的是自带的werkzeug服务器，而部署线上时，一般采用gunicorn或者uwsgi作为代理，所以我们需要配置一套自动部署的方案。在之前的__init__.py文件中，我们通过setting.yaml文件获取到了当前机器的配置信息，从而使得Flask启动时能够自动识别应该开启调试模式还是生产模式，当属于生产模式时，我们应该将werkzeug服务器挂载为代理转发模式，对接到生产类服务器上,如gunicorn。

当部署生产环境时，网络优化的任务则会交由configm.py文件进行调控，再后面章节中细讲。

#六、 关于数据预加载和内存消耗 
之前提到，Flask工程可以把模块、数据集都在服务启动前预加载到内存之中，类似机器学习生成的二进制模型之类，通常我们会伴随着服务启动变将其载入内存，加快后面接口执行相关任务时的资源调用速度。由于flask本身内核的内存资源占用极小，合理的运用这项行为可以提高项目的整体服务性能。

在Flask工程中，通常我会把需要预加载的资源放到resource目录下，包含一些字典文件、静态资源和多媒体资源等。然后在database目录下注册一个用于管理静态资源的模块,假设为res_manager.py。这个模块可以将资源进行分类读取，转换成列表或字典的形式存到内存中，然后在__init__.py文件中实例化供全局调用。

同理，数据库类型的资源也可以使用这样的方案，只要你能通过python支持数据库交互，包含mysql,mongoDB,redis等。

#七、数据库的开放性选择
redflask提供了两种数据库的简易交互方案,redis和mysql。我们先看redis:

![dababase](https://redtreeblog-1253690989.cos.ap-guangzhou.myqcloud.com/flask/2.png)

redis.py

    # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
    #当redis IO操作较为频繁的时候，应将redis对象在FLask工程中全局初始化。
    import redis
    
    def connect_redis():
        # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        return r
    
    def add_kv(redis_obj,r_key,r_value):
        redis_obj.set(r_key, r_value)
        return 'success'
    
    def get_by_key(redis_obj,r_key):
        print(redis_obj[r_key])
        print(redis_obj.get(r_key))  # 取出键name对应的值
        print(type(redis_obj.get(r_key)))
        return 'success'
        
然后是mysql,这里我们选择了sqlalchemy这个python最通用的orm框架。

_mysql.py

    # -*- coding: utf-8 -*-
    '''
    基于sqlalchemy模块的orm基础配置,当性能不佳时，建议使用原生sql语句重写核心模块
    '''
    
    #调试模式是否开启
    DEBUG = False
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #session必须要设置key
    SECRET_KEY='~XHH!jmN]LWX/,?RTA0Zr98j/3yX R'
    
    #mysql数据库连接信息,这里改为自己的账号  #直连模式启动
    HOSTNAME = '127.0.0.1'
    PORT = '3310'
    DATABASE = 'dbname'
    USERNAME = 'root'
    PASSWORD = 'root'
    #链接模式
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
    
在配置好数据库的链接信息后，便可以根据业务表建立对象模型文件,如sys_user.py:

    import json
    from __init__ import Base_mysql
    from sqlalchemy import (Column, String, Integer)
    
    # 定义好一些属性，与user表中的字段进行映射，并且这个属性要属于某个类型
    class Sys_user(Base_mysql):
        __tablename__ = 'sys_user'
    
        xid = Column(Integer, primary_key=True)
        userid = Column(String(50))
        nickname = Column(String(50))
        salt = Column(String(16))
        password=Column(String(32))
        del_flag= Column(Integer)
        create_time=Column(Integer)
        update_time=Column(Integer)
        role = Column(String(50))
        create_user = Column(String(50))
        ban_flag = Column(Integer)
    
        def __repr__(self):
            get_data = {"id":self.id, "userid":self.userid, "nickname":self.nickname, "salt":self.salt,
                        "password":self.password, "del_flag":self.del_flag, "create_time":self.create_time, "update_time":self.update_time,"role":self.role,"create_user":self.create_user
                        ,"ban_flag":self.ban_flag}
            get_data = json.dumps(get_data)
            return get_data
            
在数据库基础配置和表映射都建立好后，我们便可以在init.py中注册并实例化相关组件，然后在各类utils或service文件中调用sqlalchemy组件进行curd操作了。如果遇到性能瓶颈时，建议使用pymysql编写原生sql语句处理业务。

    from sqlalchemy import create_engine  #加载配置文件内容
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    
    from database.sqlalchemy import _mysql  # 连接数据库的数据
    
    engine_mysql = create_engine(_mysql.DB_URI, echo=False, pool_recycle=3600) # 创建引擎
    Base_mysql = declarative_base(engine_mysql)
    DBSession_mysql = sessionmaker(bind=engine_mysql) # sessionmaker生成一个session类 此后DBSession_mysql将可在全局作为一个数据库会话对象持续服务,不用重复创建

#八、 加密/验证等基础模块的实现
在redflask工程的utils目录下，提供了几项通用工具类,包含加密验证工具和装饰器。

![auth](https://redtreeblog-1253690989.cos.ap-guangzhou.myqcloud.com/flask/3.png  )

首先是encrypt.py:

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
        
此工具提供了一个通用数据库用户密码加密方案，你可以自定义使其更复杂化，甚至模仿实现类似java,shiro的效果。

然后是装饰器部分，先看dasyncio.py:

    # -*- coding: utf-8 -*-
    '''
      基于python Threading模块封装的异步函数装饰器
    '''
    from threading import Thread
    import time
    
    '''
    async_call为一次简单的异步处理操作，装饰在要异步执行的函数前，再调用该函数即可执行单次异步操作(开辟一条新的线程)
    '''
    def async_call(fn):
        def wrapper(*args, **kwargs):
            Thread(target=fn, args=args, kwargs=kwargs).start()
        return wrapper
    
    '''
    async_pool为可定义链接数的线程池装饰器，可用于并发执行多次任务
    '''
    def async_pool(pool_links):
        def wrapper(func):
            def sub_wrapper(*args,**kwargs):
                for x in range(0,pool_links):
                    Thread(target=func, args=args, kwargs=kwargs).start()
                    #func(*args, **kwargs)
            return sub_wrapper
        return wrapper
    
    '''
    async_retry为自动重试类装饰器，不支持单独异步，但可嵌套于 call 和 pool中使用
    '''
    def async_retry(retry_times,space_time):
            def wrapper(func):
                def sub_wrapper(*args, **kwargs):
                    try_times = retry_times
                    while try_times > 0:
                        try:
                            func(*args, **kwargs)
                            break
                        except Exception as e:
                            print(e)
                            time.sleep(space_time)
                            try_times = try_times - 1
                return sub_wrapper
            return wrapper
    
    # 以下为测试案例代码
    #
    # @async_call
    # def sleep2andprint():
    #     time.sleep(2)
    #     print('22222222')
    #
    # @async_pool(pool_links=5)
    # def pools():
    #     time.sleep(1)
    #     print('hehe')
    #
    #
    # @async_retry(retry_times=3,space_time=1)
    # def check():
    #     a = 1
    #     b ='2'
    #     print(a+b)
    #
    # def check_all():
    #     print('正在测试async_call组件')
    #     print('111111')
    #     sleep2andprint()
    #     print('333333')
    #     print('若3333出现在22222此前，异步成功')
    #     print('正在测试async_pool组件')
    #     pools()
    #     print('在一秒内打印出5个hehe为成功')
    #     print('正在测试async_retry组件')
    #     check()
    #     print('打印三次异常则成功')
    #
    # check_all()
    
异步装饰器可以使工程中的任意函数单独开辟一条额外的线程去执行特殊业务，比如用户行为纪录，以确保用户的在执行操作时不受系统纪录行为的结果影响。

token_manager.py:

    # -*- coding: utf-8 -*-
    '''
    服务端token验证器
    '''
    
    import time
    import base64
    import hmac
    from __init__ import make_response,request
    
    #生成token
    def generate_token(key, expire=1800):
        r'''
            @Args:
                key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
                expire: int(最大有效时间，单位为s)
            @Return:
                state: str
        '''
        ts_str = str(time.time() + expire)
        ts_byte = ts_str.encode("utf-8")
        sha1_tshexstr  = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest()
        token = ts_str+':'+sha1_tshexstr
        b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
        return b64_token.decode("utf-8")
    
    #token校验
    def certify_token(key, token):
        r'''
            @Args:
                key: str
                token: str
            @Returns:
                boolean
        '''
        token_str = base64.urlsafe_b64decode(token).decode('utf-8')
        token_list = token_str.split(':')
        if len(token_list) != 2:
            return False
        ts_str = token_list[0]
        if float(ts_str) < time.time():
            # token expired
            return False
        known_sha1_tsstr = token_list[1]
        sha1 = hmac.new(key.encode("utf-8"),ts_str.encode('utf-8'),'sha1')
        calc_sha1_tsstr = sha1.hexdigest()
        if calc_sha1_tsstr != known_sha1_tsstr:
            # token certification failed
            return False
        # token certification success
        return True
    
    #token校验
    def auth_check(func):
        def inner(*args,**kwargs):
            try:
                key = request.cookies.get('key')
                token = request.cookies.get('token')
    
                if certify_token(key,token) == True:
                    pass
                else:
                    return 'Auth-Error'
            except Exception as e :
                return 'Auth-Error'
            return func(*args,**kwargs)
        return inner

提供了auth_check装饰器，用于校验用户的请求合法性或者客户端cookie的有效期。

pub_decorator.py中则是提供了一些关于失败任务自动重新调度的解决方案，由于大部分程序在出现异常时会有对应的抛出和解决方案，这里就不细说，感兴趣的小伙伴自行翻看下源码便可理解。

值得一提的是，在引入装饰器修饰接口函数时，会涉及到一个问题:flask路由的节点冲突。所以，当有多个接口同时调用一个装饰器时，必须为接口的路由配置不同的节点名，请看下一章。

#九、节点映射和装饰器的使用
回到apis.py文件中来，我们看文件的最下面部分。

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
       
flask默认将路由的的函数名作为endpoint的标识名。通常情况下不会出现路由之间节点冲突的问题。但当两个路由都被装饰器修饰时,endpoint会读取到类似匿名函数的节点名从而分配給默认的greeting节点上引发冲突。所以要为不同路由手动添加endpoint。

#十、并发处理及网络模型的选择

大部分web框架在设计时，为了方便本地调试代码，会封装一个简易httpserver,少部分web框架本身就是一个强力的webserver(tonardo)。werkzeug对于Flask来说，便是对wsgi实现了一个简单封装，让flask能专注于application的业务逻辑本身，将网络层的模式设计交由其他模块拓展。在本次教程中，我会对python常用的httpserver及网络模型做个简单介绍，但不会深入讲解，重点依然是让读者快速上手框架的整体结构并用于实战。

wsgi：Web Server Gateway Interface。
关于wsgi，这里我摘录了廖大的一段解释，讲得很清楚了。
    
    （摘录至廖雪峰个人网站）
    了解了HTTP协议和HTML文档，我们其实就明白了一个Web应用的本质就是：
    
    浏览器发送一个HTTP请求；
    
    服务器收到请求，生成一个HTML文档；
    
    服务器把HTML文档作为HTTP响应的Body发送给浏览器；
    
    浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。
    
    所以，最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。
    
    如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范。
    
    正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务
    
也就是说，wsgi被作为python最通用的http协议接口，大量的python_web_application 与 python_http_server都是基于wsgi构建的。而其中最常用的server便是uwsgi和gunicorn。

他们之间的异同点主要如下:
1 uwsgi和gunicorn 都过 pre-fork 方式增加 server 并发处理能力。
2 在不采用网络模型优化的情况下，两者皆采用默认形态，在高并发情况下，gunicorn的响应时间会快于uwsgi,但丢包率稍高，且吞吐量较低。
3 gunicorn的配置较为简单，且具备较多网络模型可选择：select、epoll、gevent、meinheld等。
4 gunicorn默认仅支持部署unix系统，uwsgi则支持部署windows。
5 两者都能完美搭配nginx使用。

由于gunicorn对gevent和meinheld这两个目前性能最优秀的通用网络模型有较好的支持，且配置启动方式极其简洁，redflask选用gunicorn作为WSGIserver。

网络模型的选择: gevent vs meinheld，两者都是基于python的greenlet库实现协程。

    meinheld：greenlet(协程) + picoev（高性能网络库） 
    gevent：greenlet（协程） + libevent（高性能网络库）

协程：又称微线程，纤程。 
协程的这种“挂起”和“唤醒”机制实质上是将一个过程切分成了若干个子过程，给了我们一种以扁平的方式来使用事件回调模型。优点：共享进程的上下文，一个进程可以创建百万，千万的coroutine。

picoev  vs libevent 
picoev在项目下有把picoev和libevent这些库做对比，作者也提了一下为什么picoev的速度会这么快。主要有两个原因。 

    1. picoev几乎所有顺序结构都是用数组实现的，索引访问速度比libevent的链表快很多。 
    2. picoev采用了环形队列+vector+bitmap来实现定时事件的检测。
    
好了，我们再来看下gevent和meinheld的设计理念不同之处:

Gevent

    1. 先通过Timer最小堆（以时间为排序的键）找出至少要等待的时间。（代码中的timeout_next()函数）。 
    2. 通过select发送这些事件fd到内核并设置时间为1中所求的等待时间。然后把select返回的就绪事件放到就绪列表。（对应 evsel->dispatch(base, evbase, tv_p)）。 
    3. 然后把现在超时的计时事件放到就绪列表。（对应gettime(base, &base->tv_cache)）。 
    4. 最后调用处理函数处理就绪列表中的事件（timeout_process(base)）。

MeinHeld

    概要：双轮询异步非阻塞模型
    MeinHeld是目前python_web网络框架中的性能怪兽，douban、知乎都应用了这个设计模式。
    MeinHeld基于Gunicorn的基础上，能根据不同机器的cpu内核性能自动调整worker进程(的数量)，
    并且每个worker下的工作子进程也会根据cpu作调整，保持在一个最佳性能区间。以下是meinheld的几个优秀之处：
    1 meinheld的master_worker可设置为damon模式，即守护进程模式。unix系统中，守护进程将拥有最高级的内存使用权限，master_worker可以自动托起挂死进程，重新分配内存。
    2 meinheld 的 双轮巡机制，首先是slave_worker间的轮询，meinheld采用了master和slave间的双向交互，一旦slave进程上报请求结果，将自动进入空闲队列，master在作完记录后优先向空闲进程分配http请求。其次，每个worker也对自己的子线程进行轮询，每轮轮巡完毕后会向master_worker上报空闲thread数量和上次请求完成时间点。 双轮巡的机制能够完美的利用所有线程，达到最佳访问性能。
    
（下面是关于meinheld的timeout_队列原理图和一段说明，部分摘自csdn,但原作者不详，若有侵权请联系作者。）

![4](https://redtreeblog-1253690989.cos.ap-guangzhou.myqcloud.com/flask/4.jpg)

    对于timeout环形队列，每经过resolution时间就往后移动一块，当前队头永远指向刚刚到达时间的事件块，如图当前处理的是2，那么说明队列头在2，那么再经过resolution时间就会到3，根据时间不断后移，循环利用。
    1. 在处理每一块timeout里面注册的事件时，遍历所有不为0的vector，得出对应的fd。图中已经写的很清楚的，其实原理和16进制一样简单。插入一个事件的时间复杂度为O(1),遍历所有在timeout块的注册事件时间复杂度等价为O(n)[注：这里n为timeout里面注册事件的个数]，对比libevent的最小堆O(logn)插入，每次处理一个后调整堆的复杂度O(logn)处理n个就为O(nlogn)，确实是高效很多。
    2. 还有一个高效的地方在于，meinheld是检测到有一个事件就马上处理（无阻塞），不像gevent挂起等待最小等待时间到达（阻塞），然后才对所有就绪事件队列里面的事件进行处理，不过这也导致了meinheld不能设定事件处理的优先级。
    
    简单来说就是，master进程将任务分发给上一轮上报后空闲thread数量最多的slaver,接到请求的slaver分发给空闲thread后重新上报给master.反复操作。另外当线程死锁时，master会释放掉slaver重建worker.    

现在，我们来举个直观的例子，假设现在有一个足球场，有个教练在一边的底线负责给球员传递足球，场上的球员接到球后要将球带到对面的球门里并返回上报结果。

    1 、当Flask仅作为一个简易server时，可以这么理解:
        只有一个教练和一个球员在执行这项任务。
    2 、当引入gunicorn代理时，假设我们fork4个worker,这时候是这样:
        还是只有一个教练，但多了4个球员来完成这项任务。教练依旧是把球往地上一扔，4个人谁跑得快先搞定任务就拿走下个球。
    3 、当引入gunicorn+gevent模式的时候,我们引入组员的概念，还是有4个球员，但是他们通过自己的手段各自号召了若干个小弟来完成任务:
        这时候教练会纪录每个球员之间完成任务的速度，比如A1分钟4个，B3C2D1这样子，那么教练会优先把球分配给之前做得快球员，可能一次性给多个球过去。
    4 、当使用meinheld时，假设有一个教练，4个组，每组人数若干：
        教练一开始看哪个组的空闲人数比较多，就优先发给那个组的组长，组长接过球后再把球分发给空闲的组员。另外，教练还要充当全程保姆，一旦发现哪个组干活效率出问题了，或者不同的球员踢了同一个球，或者有球员受伤了，他会立马替换新球员。

OK，说了这么多，我们来看一下如果在redflask工程中编写gunicorn代理的基础配置，这是根目录下的configm.py文件:

    '''
    Gunicorn的配置文件，默认选用gevent模型，有兴趣的话可以自己研究下更强大的meinheld。
    '''
    import multiprocessing
    
    #ssl证书 如果需要部署https协议的服务则使用下列命令
    #certfile="server.crt"
    #keyfile="server_nopwd.key"
    
    # 监听本机的5000端口
    bind = '0.0.0.0:5000'
    
    preload_app = True
    
    # 开启进程
    workers=4
    #workers = multiprocessing.cpu_count() * 2 + 1
    
    # 每个进程的开启线程
    threads = 10
    backlog = 2048
    
    # 工作模式为meinheld
    #worker_class = "egg:meinheld#gunicorn_worker"
    #gevent
    worker_class = "gevent"
    
    # debug=True
    # 如果不使用supervisord之类的进程管理工具可以是进程成为守护进程，否则会出问题
    daemon = False
    
    # 进程名称
    proc_name = 'red_flask.pid'
    
    # 进程pid记录文件
    pidfile = 'app_pid.log'
    
    loglevel = 'debug'
    logfile = 'log/red_flask_debug.log'
    accesslog = 'log/red_flask_access.log'
    access_log_format = '%(h)s %(t)s %(U)s %(q)s'

可以看出，gunicorn的配置文件十分简洁。通过更改worker_class即可在gevent和meinheld中进行模式切换，另外还能根据cpu内核数量进行进程调控，支持https等。

在编写完成configm.py后，我们便可以通过gunicorn启动flask的生产服务。

    1、pip install -r requirements.txt (包含gunicorn、gevent、meinheld等依赖)
    2、终端输入 gunicorn -c configm.py run:app 
    3、通常在linux环境下，我们会编写一个shell文件，通过nohup命令将gunicorn服务部署到系统后台。

#十一、 服务端部署方案详解
在商用场景中，flask+gunicorn的组合并不够完善，通常我们还需要结合另外两个软件，即Nginx+Supervisor。

Nginx是一个高性能的Http和反向代理服务器,对wsgiServer完美支持。通常我们会把后端服务挂载在Nginx的端口服务下，让Nginx进行请求转发。同时，Nginx还具备执行静态资源处理，资源限制，gzip,负载均衡等功能，十分强大。

Supervisor则是一个由python编写的后台进程管理工具,程序托管在supervisor的时候可以实现自重启，缓加载更新等功能。

下面就来介绍如何在一台linux服务器上部署redflask服务:(以下以ubuntu为例子)

1、通过git或scp将代码上传到服务器。（略）
2、通过gunicorn启动redflask。（略）
3、安装部署nginx,并配置代理到gunicorn
4、安装部署supervisor,并配置gunicorn服务

**Nginx的对应配置**

**如何安装**

如果您是ubuntu系统,并且不需求nginx的最新特性，那么完全可以通过apt市场进行快速安装。 
安装nginx前，需要先安装相关依赖，包括： 

安装gcc g++的依赖库 
ubuntu平台可以使用如下命令。 

**1 gcc g++ 模块**

    apt-get install build-essential 

    apt-get install libtool 

**2 pcre 依赖** 

    sudo apt-get update 

    sudo apt-get install libpcre3 libpcre3-dev 

**3 zlib 依赖** 

    apt-get install zlib1g-dev 

**4 ssl 依赖库** 

    apt-get install openssl

**然后就是** 
    
    sudo apt-get install nginx

ubuntu会自动帮你完成系统服务的配置，之后可以通过命令: 

**修改nginx配置：**

    sudo vim /etc/nginx/nginx.conf  

**启动服务** 

    service nginx start 

打开浏览器，访问本机ip地址，看到welcome to nginx界面，表示安装成功。

**NGINX主要功能**

**1、静态HTTP服务器**

首先，Nginx是一个HTTP服务器，可以将服务器上的静态文件（如HTML、图片）通过HTTP协议展现给客户端。

    server { 
    listen80; # 端口号 
    location / { 
    root /usr/share/nginx/html; # 静态文件路径 
    } 
    }

**2、反向代理服务器** 
    
    server { 
    listen80; 
    location / { 
    proxy_pass http://192.168.20.1:8080; # 应用服务器HTTP地址 
    } 
    }

**3、负载均衡** 
    
    upstream myapp { 
    server192.168.20.1:8080; # 应用服务器1 
    server192.168.20.2:8080; # 应用服务器2 
    } 
    server { 
    listen80; 
    location / { 
    proxy_pass http://myapp; 
    } 
    } 
    
以上配置会将请求轮询分配到应用服务器，也就是一个客户端的多次请求，有可能会由多台不同的服务器处理。可以通过ip-hash的方式，根据客户端ip地址的hash值将请求分配给固定的某一个服务器处理。 
    
    upstream myapp { 
    ip_hash; # 根据客户端IP地址Hash值将请求分配给固定的一个服务器处理 
    server192.168.20.1:8080; 
    server192.168.20.2:8080; 
    } 
    server { 
    listen80; 
    location / { 
    proxy_pass http://myapp; 
    } 
    } 
    
另外，服务器的硬件配置可能有好有差，想把大部分请求分配给好的服务器，把少量请求分配给差的服务器，可以通过weight来控制。 
    
    upstream myapp { 
    server192.168.20.1:8080weight=3; # 该服务器处理3/4请求 
    server192.168.20.2:8080; # weight默认为1，该服务器处理1/4请求 
    } 
    server { 
    listen80; 
    location / { 
    proxy_pass http://myapp; 
    } 
    } 
**4、虚拟主机** 
有的网站访问量大，需要负载均衡。然而并不是所有网站都如此出色，有的网站，由于访问量太小，需要节省成本，将多个网站部署在同一台服务器上。

例如将www.aaa.com和www.bbb.com两个网站部署在同一台服务器上，两个域名解析到同一个IP地址，但是用户通过两个域名却可以打开两个完全不同的网站，互相不影响，就像访问两个服务器一样，所以叫两个虚拟主机。

    server { 
    listen80default_server; 
    server_name _; 
    return444; # 过滤其他域名的请求，返回444状态码 
    } 
    server { 
    listen80; 
    server_name www.aaa.com; # www.aaa.com域名 
    location / { 
    proxy_pass http://localhost:8080; # 对应端口号8080 
    } 
    } 
    server { 
    listen80; 
    server_name www.bbb.com; # www.bbb.com域名 
    location / { 
    proxy_pass http://localhost:8081; # 对应端口号8081 
    } 
    } 

**简易爬虫过滤方案**

    location / { 
    if ($http_user_agent ~* "python|curl|java|wget|httpclient|okhttp") { 
    return 503; 
    } 
        #正常处理 
    ... 
    } 
这个是在廖雪峰博客上看到的，原文为： 
现在的网络爬虫越来越多，有很多爬虫都是初学者写的，和搜索引擎的爬虫不一样，他们不懂如何控制速度，结果往往大量消耗服务器资源，导致带宽白白浪费了。

其实Nginx可以非常容易地根据User-Agent过滤请求，我们只需要在需要URL入口位置通过一个简单的正则表达式就可以过滤不符合要求的爬虫请求：

变量$http_user_agent是一个可以直接在location中引用的Nginx变量。~*表示不区分大小写的正则匹配，通过python就可以过滤掉80%的Python爬虫

**其他功能**

自行探索吧。

**supervisor的对应配置**
服务端运维的重点，系统中各类进程的守护者。由于不支持python3的环境，所以配置会稍微麻烦一点,我们需要通过virtualenv 创建一个python2虚拟环境。

    pip install virtualenv

首先在自定义目录下创建 super 虚拟环境

    virtualenv --distribute -p /usr/bin/python2 super

    cd super
    source bin/activate    #激活虚拟环境
    ./bin/pip install supervisor# 安装supervier
    echo_supervisord_conf > supervisor.conf   # 生成 supervisor 默认配置文件

    #热后便可以通过以下命令对supervisor进行操作：
    supervisord -c supervisor.conf #通过配置文件启动supervisor
    supervisorctl -c supervisor.conf status #察看supervisor的状态
    supervisorctl -c supervisor.conf reload 重新载入 #配置文件
    supervisorctl -c supervisor.conf start [all]|[appname] #启动指定/所有 supervisor管理的程序进程
    supervisorctl -c supervisor.conf stop [all]|[appname] 关闭指定/所有 supervisor管理的程序进程

supervisor.conf中配置对应的gunicorn应用,其他类型的应用配置也类似，比如java的springboot。

    [program:start_gunicorn]
    command=/your/bin/path/to/gunicorn -w 4 -b 0.0.0.0:5000 -k gevent run:app
    directory:/home/ubuntu/project/test1/ #run.py所在的目录
    autostart=true
    redirect_stderr=true
    user=root
    directory=/usr/local/qs-project/web
    stdout_logfile=/var/log/test_test.log

如果要启用supervisor的web端：9001端口.

需要注释掉 配置文件中

[inet_http_server]  的所有子配置项

以及

[supervisorctl] 中的前四项

    deactivate  #退出环境

**至此，教程结束,第一次编写小册，如有错误或不足，欢迎指正、交流。**

# red_flask

#### 项目介绍

    Restful framework base on flask without blueprint. 
    一个基于Flask搭建的Restful_Api服务框架,实现了路由分离的功能但无需依赖于Flask的蓝本。提供了常用的http请求类型和文件传输类型的相关接口。
    提供了较简单的异步任务分发方案。提供了最常用的用户密码校验模块和token验证模块(集成Oauth2)。集成了Gunicorn+Gevent的服务器自动配置方案。
    数据库ORm使用flask_sqlalchemy,迁移工具使用flask_migrate(旧版本的sqlalchemy已弃用)
    提供了Flask作为Https服务的解决方案。解决了Flask跨域问题。双系统生产化部署(windows/linux)。

#### 通过PIP快速构建redflask工程

    1. pip install redflask==0.1.5
    2. redflask -b [your_project_name]

#### 通过github获取源码

    1. 使用 git clone 命令将项目复制到本地
    2. pip install -r requirements.txt 安装所有依赖

#### 使用说明

    1. 本地调试，直接python run.py (请在config.py中配置WEB_IP为localhost)
    2. 部署调试，chmod +x test.sh  然后 ./test.sh
    3. 部署生产, chmod +x start.sh 然后 ./start.sh

#### 工程目录架构

        
    controller(目录) : 路由控制器，用来注解并分配工程的api地址和分发对应的接口任务，
                       其作用类似于Java SpringBoot 中的restcontroller.子下的文件目录根据对应业务类型进行区分  
                       
    database(目录):  mysql-orm 文件目录 
                    其中orms.py用于注册所有使用到的model,
                    orm_tool.py用来辅助生成orm的__init__/__repr__方法
                    
    init_settings(目录): 放置系统初始化数据的配置文件和脚本。如系统菜单/字典/表单/流程的配置
    
    log(目录): 用于存放服务生成的日志文件
    
    migrations: flask_migrate生成的文件目录，用于管理数据库版本文件和迁移脚本
    
    res : 如果采用本地化对象资源存储，则使用此目录，若使用云对象存储服务器，则忽略。
          cache : 存放系统生成的缓存文件
          prefab : 存放系统预置的多媒体文件和文档数据
          upload : 存放用户上传的多媒体文件或文档数据
    
    service: 用于编写API实际业务逻辑的文件目录，
             Controller下的api接口一般会从此处调用具体服务，
             其目录结构与controller的API业务对应。
             
    test_case : 测试案例写在这里,请保持目录结构与controller的API业务对应。
    
    utils: 泛用工具类及全局装饰器的存储目录。    
           common :  如编码规则生成器，加解密工具，算法等第三方常用拓展
           decorator : 常用的全局装饰器，如自定义异步任务/Oauth2接口认证等
           http : 基于flask的http-requeset请求，实现get/post方法的自动参数匹配和请求返回错误码自定义。规范联调。
           
    __init.py__ :  flask_app的工程初始化配置文件，常用的flask服务组件需在此全局初始化。
                 另外，由于取消了Flask蓝图的使用,所以controller中的业务接口需要在此注册才能生效。
            
    config.py : 用于部署Flask工程的基础配置文件，包含本地部署配置/数据库连接配置/数据查询习惯配置等    
    
    db_migrate_manager : 数据库迁移脚本控制器
    
    gunicorn_config.py : Linux环境下，使用Gunicorn部署Flask的配置脚本
          
    requirements.txt 记录依赖模块 方便pip安装
    
    run.py 服务启动入口，wsgi配置文件
    
    start.sh 服务启动脚本
    
    test.sh 测试脚本

#### 参与贡献

    感谢吴航/郑松银/黄应飞 提供的部分架构思路

#### 版本更新日志

    20190802 
    1  添加常用的正则校验工具  utils/common/regex_matcher.py
    2  添加redis常用的操作函数 utils/common/redisor.py
    3  添加文本相似度通用算法工具  utils/common/text_similarity.py
    4  添加xls，excel文本读写工具  utils/common/xls_tool.py
    5  添加Flask框架对用户请求的参数校验工具及错误类型封包 utils/http/responser.py
    20191202
    1 添加常用的消息队列、分布式任务框架案例，celery+rabbitMQ。 utils/msg_queue
    2 添加一个快捷日志纪录工具。 utils/common/logger.py
    20200416
    1 service中添加了一个常规的系统用户表CRUD操作，并在controller中实现了对应接口，对应的数据库已转存为.sql文件存放在 database/sql_bak目录下
    2 utils/decorator 目录下添加了目前最常用的基于token的Oauth2认证装饰器，区别于之前将token存储于浏览器cookie中的方案，客户端可以自由选择如何存储token.
    3 contorller/service 中 提供了使用http_resonser的案例，可以对接口传参进行自动校验并返回对应的错误码。
    4 添加zip解析工具
    5 为windows环境下的生产化部署提供了新的方案，基于tornado做一层转发，性能未知。
    6 配置文件新增了部署端口、数据库常量配置、系统超时时间、加密方式等字段
    20210412
    1 ORM舍弃原生的sqlalchemy,改用flask_sqlalchemy,原因是flask_sqlalchemy在自动回收数据库连接方面做的更好
    2 数据库迁移工具弃用alembic,改用flask_migrate,使用起来更简洁。
    3 修改了项目架构，去除了一些过分细节化的模块。只保留重要的演示模块。
    4 用户表预置接口只保留登录功能，删除了原本的增删改查业务（懒得写了）
    5 

## 设计理念

    我并不打算把这个框架做的很细致全面，尽管他在企业级应用中已经有了许多复杂的变化。
    我只是想分享这个框架的设计思路，所以尽量保留一个简洁的版本。
    框架的目的是使多人合作开发的过程中，每个人能很清楚代码的结构，快速定位自己coding的模块。
    
    ===========================
    接下来这个框架可能再也不会更新了，纪念我的python-coding之路。-----20210412 



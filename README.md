# red_flask

#### 项目介绍

Restful framework base on flask without blueprint.

一个基于Flask搭建的Restful_Api服务框架,实现了路由分离的功能但无需依赖于Flask的蓝本。提供了常用的http请求类型和文件传输类型的相关接口。

提供了较简单的异步任务分发方案。提供了最常用的用户密码校验模块和token验证模块。集成了Gunicorn+Gevent的服务器自动配置方案。数据库端使用

Sqlalchemy和Redis。提供了Flask作为Https服务的解决方案。解决了Flask跨域问题。

#### 软件架构

controller : 路由控制器，用来注解并分配工程的api地址和分发对应的接口任务，其作用类似于Java SpringBoot 中的restcontroller.子下的文件目录根据对应业务类型进行区分

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

#### 安装教程

1. 使用 git clone 命令将项目复制到本地
2. pip install -r requirements.txt 安装所有依赖


#### 使用说明

1. 本地调试，直接python run.py (请在setting.yaml中配置IP为localhost)
2. 部署调试，chmod +x test.sh  然后 ./test.sh
3. 部署生产, chmod +x start.sh 然后 ./start.sh

#### 参与贡献

感谢航小妈提供的部分架构思路


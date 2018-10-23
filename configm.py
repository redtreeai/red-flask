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
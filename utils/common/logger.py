# -*- coding: utf-8 -*-
# @Time    : 19-12-2 下午3:48
# @Author  : Redtree
# @File    : logger.py
# @Desc :  调用python内置的logging模块实现日志管理，配置log.IO等框架实现日志可视化管理。

import logging
from __init__ import  ROOT_PATH

def set_log(logWord,level='warning',logName='error'):


    log_path = ROOT_PATH+'/log/'+str(logName)+'.log'
    logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=log_path,
                            filemode='a')

    #一般采用warning 级别  日志即可

    if level=='warning':
        logging.warning(logWord) #warning  警告级别日志  会在控制台输出
    elif level=='info':
        logging.info(logWord)   #info 消息备注 只能在log文件输出
    elif level=='error':        # 普通错误 会在控制台输出
        logging.error(logWord)
    elif level=='critical':    #严重错误 会在控制台输出
        logging.critical(logWord)
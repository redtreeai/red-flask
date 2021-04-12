# -*- coding: utf-8 -*-
# @ Time   :  2021/4/6 14:46
# @ Author : Redtree
# @ File :  db_manager 
# @ Desc :  单独将flask_migrate部分功能移出，不与flask_app本地IDE工具调试冲突。


from __init__ import manager
manager.run()


'''
在工程根目录下，运行
python db_migrate_manager.py db init
python db_migrate_manager.py db migrate
python db_migrate_manager.py db upgrade
python db_migrate_manager.py db --help
'''
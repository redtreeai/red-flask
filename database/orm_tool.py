# -*- coding: utf-8 -*-
# @Time    : 18-11-7 下午3:56
# @Author  : Redtree
# @File    : orm_tool.py
# @Desc :  ORM 文件编写辅助工具，快速生成__init__/__repr__定制,有空再升级.


def dojob():

    #class_data中填入orm_class的基础属性

    class_data = '''
    uuid = Column(Integer, primary_key=True)
    username = Column(String(50))
    nickname = Column(String(50))
    salt = Column(String(16))
    password=Column(String(32))
    del_flag= Column(Integer)
    created_time=Column(Integer)
    updated_time=Column(Integer)
    created_user = Column(String(50))
    '''

    '''
    执行dojob函数，获得如下输出：
      def __init__ (self,uuid,username,nickname,salt,password,del_flag,created_time,updated_time,created_user):
     self.uuid = uuid
     self.username = username
     self.nickname = nickname
     self.salt = salt
     self.password = password
     self.del_flag = del_flag
     self.created_time = created_time
     self.updated_time = updated_time
     self.created_user = created_user
     def __repr__(self):
      obj={
         "uuid" : self.uuid,
         "username" : self.username,
         "nickname" : self.nickname,
         "salt" : self.salt,
         "password" : self.password,
         "del_flag" : self.del_flag,
         "created_time" : self.created_time,
         "updated_time" : self.updated_time,
         "created_user" : self.created_user
      }
      return json.dumps(obj)

Process finished with exit code 0

    '''

    lines = class_data.split('\n')
    #initlist
    r1 = "  def __init__ (self,"
    for l in lines:
        if l.__contains__('='):
            name = l.split('=')[0].replace(' ', '')
            if not name=='mp_id':
                r1=r1+''+name+','
    r1 = r1[:-1]
    r1 = r1+'):'
    print(r1)
    for l in lines:
        if l.__contains__('='):
            name = l.split('=')[0].replace(' ', '')
            if not name=='mp_id':
                print("     "+'self.' + name + ' = ' + name)
    r2 = "  def __repr__(self):"
    print(r2)
    r3 = "      obj={"
    print(r3)

    new_lines = []
    for l in lines:
        if l.__contains__('='):
            new_lines.append(l)
    ll = len(new_lines)
    index = 0
    for l in new_lines:
        if l.__contains__('='):
            name = l.split('=')[0].replace(' ','')
            index+=1
            if index<ll:
                print("         "+'\"'+name+'\"'+' : '+'self.'+name+',')
            else:
                print("         "+'\"'+name+'\"'+' : '+'self.'+name)
    r4 = "      }"
    print(r4)
    r5 = "      return json.dumps(obj)"
    print(r5)


dojob()

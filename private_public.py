#-*- coding:utf-8 -*-
'文件注释'
__author__='wh'

class Priv():
    def __init__(self,name,age):
        self.__name=name
        self.__age = age
    def print_info(self):
        print("private的内部信息为: name= %s,age= %d"%(self.__name,self.__age))
    def __prvfunc(self):
        print("我是私有方法")
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
   
class Pub():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_info(self):
        print("public的内部信息为: name= %s,age= %d"%(self.name,self.age))
p = Priv('wh',29)
p.print_info()
#print(p.__name)
print(p._Priv__name)
pb = Pub('wh',29)
print(pb.name,pb.age)
#p.__prvfunc()
p._Priv__prvfunc()
p.set_name('wh2')
p.get_name()
''' 私有变量和方法被python解释器名'''

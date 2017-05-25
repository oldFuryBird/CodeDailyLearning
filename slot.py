#-*- coding:utf-8 -*-
'slots'
__author__='wh'
class Student():
    __slots__=('name','age')


s = Student()
s.age = 1
s.name='wh'
#s.score=111
'''score被禁止实例会报AttributeError
    __slots 只对当前类起作用，对子类无效

'''

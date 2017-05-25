#-*- coding:utf-8 -*-
'继承 与多态'
__author__='wh'

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')
        
class Cat(Animal):
    def run(self):
        print('Cat is running')
def run_twice(Animal):
        Animal.run()
        Animal.run()
class Student():
    def run(self):
        print('People is walking')
dog = Dog()
run_twice(dog)
stu = Student()
run_twice(stu)
'''
接口函数run_twice  只需要参数类有run方法就可以调用，不需要检查类型
'''

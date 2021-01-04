# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:25:57 2020

@author: mmm
"""


class Person():
    def __init__(self, name, age,idnum):
        self.name = name
        self.age = age
        self.idnum =idnum
    def output(self):
        print(("your name is :" + self.name  +"your age is : " + self.age + "youridnum is :"+self.idnum))  
class Man():
    def strong(self):
        print("mens are strong")
class Child( Person , Man):
    pass
kid = Child('john','23','101')
kid.output()
kid.strong()
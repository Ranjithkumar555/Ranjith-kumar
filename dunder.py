# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 19:57:15 2020

@author: mmm
"""


class Person():
    def __init__(self,name):
        self.name = name
    
    def __call__(self,y):
      
        print("call this function",y)
p = Person('y')
p(4)


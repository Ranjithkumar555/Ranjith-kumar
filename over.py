# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 12:24:48 2020

@author: mmm
"""


class Point():
    def __init__(self,x ,y  ):
        self.x = x
        self.y = y
       
    
    def __add__(self,p):
        return Point(self.x + p.x ,self.y + p.y)
    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ')'
   
p1 = Point(3, 4)    
p2 = Point(3, 2) 
p3 = p1 + p2
print(p3)                                        
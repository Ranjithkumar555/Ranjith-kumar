# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:22:38 2020

@author: mmm
"""


class Parrot():
    def fly(self):
        print(" parrt can fly")
    def swim(self):
        print(" parrot can't swim")
class Penguin():
    def fly(self):
        print(" penguin can't fly")
    def swim(self):
        print(" penguin can swim")

blu = Parrot()
peggy = Penguin()
for birds in(blu,peggy):
    birds.fly()
    birds.swim()



    
        
        
        
        
        
        
            
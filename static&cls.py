# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:13:22 2020

@author: mmm
"""


class Dog():
    dogs = []

    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.dogs.append(self)
        self.dogs.append(self)
       
     
    @classmethod
    def num_dog(cls):
        print( len(cls.dogs))
    @staticmethod
    def bark(n):
        for _ in range(n):
            print("bark")
tim = Dog('tim' ,'5')
tim.num_dog()
tim.bark(5)




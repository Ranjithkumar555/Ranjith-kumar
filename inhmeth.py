# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:49:56 2020

@author: mmm
"""


class Dog():
    def __init__(self ,name ,age):
        self.name = name
        self.age = age
        self.li = [1,2,3]
    def speak(self):
        print(" hi i am " + self.name + "i am" + self.age + "years old")
    def change_age(self ,age):
        self.age = age
    def add_weight(self,weight):
        self.weight = weight
tim = Dog('tim ', '23')
fred = Dog('fred','24')
tim.speak()
fred.speak()
tim.change_age(25)
tim.add_weight(70)
print(tim.speak)



        
        
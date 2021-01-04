# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 20:58:42 2021

@author: mmm
"""


class Person:
    def __init__(self,initialAge):
        self.initialage = age
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if age < 0:
            age = 0
            print("age is not valid,setting age yo 0")
            print("young")
        elif age < 13 :
            print("you are young")
        elif  age <= 13 and age < 18:
            print("you are a teenager")
        else:
            print("you are old")
            
        
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        age = age + 3
        
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:50:44 2020

@author: mmm
"""

y = [ 1000, 1000 , 1000 ,1000]
class Tendency():
    def __init__(self , x):
        self.x = x
        
    def mean1(self):
        m = self.x
        sum = 0
        for i in m:
            sum = i + sum
        mean = sum / len(m)
        return mean
    def mode1(self):
        p = self.x
        for i in p:
            
            
    def med1(self):
        s = self.x
        s.sort()
        if len(s)% 2 == 0:
            f1 = s[len(s)/2]
            
            
            
            
            
        
    
        
mn = Tendency(y)
mn.mean1()
mn.mode1()
mn.med1()
a = mn.mean1()


         
import numpy as np
np.random.rand() 

a = " hello "
a = 2
import random 
print(random.randint(0 ,100)) 


for i in range(1,1000) :
    if i < 100:
       x = random.randint(0 ,1000)
    
  
import numpy as np
np.mean(x)       
  



class Person():
    def __init__(self, name, age,idnum):
        self.name = name
        self.age = age
        self.idnum =idnum
    def output(self):
        print(("your name is :" + self.name  +"your age is : " + self.age + "youridnum is :"+self.idnum))









 
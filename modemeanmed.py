# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:31:55 2020

@author: mmm
"""







      
    
        
        
y =[1,2,3,4,2,3,2]    
            
 
class Maths():
    def __init__(self, x):
        self.x = x
        
    def mean1(self):
        m = self.x
        sum = 0
        for i in m:
            sum = sum + i
        mean = sum/len(m)
        return mean
    
    def med1(self):
        s = self.x
        if len(s) % 2 == 0:
            f1 =  s[len(s)//2]
            f2 =  s[len(s)//2 - 1]
            med = (f1 + f2) / 2
            
        else:
            r = int((len(s) - 1) /2)
            med = s[r]
            
            
        return med
        
    def mode1(self):
        p = self.x
        d = {}
        for x in p:
            if x in d:
                d[x] = d[x] + 1
            else:
                d[x] = 1
        max_occur = 0
        for key,val in d.items():
            if max_occur < val:
                max_occur = val
        l = max_occur
        print(d[l])
        return d    
     
mn = Maths(y)
mn.mean1()
mn.med1()
mn.mode1()            
     
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:42:22 2020

@author: mmm
"""





with open("d:/msc.csv","r") as file:
    t = []
    for line in file:
        line_split = line.strip().split(";")
        t.append(line_split[1])
    print(t)
    [x.strip() for x in t]
    print(t)
    d = {}                
    for i in t :
        if i in d :
            d[i] = d[i] + 1
        else:
            d[i] = 1
    print(d)
    
    
    
    
    
lst = ['name','akash','akash','bala','akash','bala','abdul','akash','dony','frank','dony']
d = {}
for i in lst:
    if i in d :
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:23:31 2020

@author: mmm
"""


for i in range(1 ,20):
    count = 0
    for j in range(1 , i + 1):
        if (i % j)== 0:
            count =count + 1
    if count == 2:
        print(i)
      
        
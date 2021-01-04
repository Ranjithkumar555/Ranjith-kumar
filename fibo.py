# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 19:42:02 2020

@author: mmm
"""
 n =int(input("enter the no:" ))    
n1 =0
n2 =1
sum =0
while n1<n :
    print(n1)
    if n1 % 2 == 0:
      sum = sum + n1
    nth = n1 + n2
    n1 = n2
    n2 = nth
print(" the sum is : " ,sum)
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:57:01 2021

@author: mmm
"""


from statistics import median
n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
t=int(len(arr)/2)
if len(arr)%2==0:
    L=arr[:t]
    U=arr[t:]
else:
    L=arr[:t]
    U=arr[t+1:]
    
print(int(median(L)))
print(int(median(arr)))
print(int(median(U)))
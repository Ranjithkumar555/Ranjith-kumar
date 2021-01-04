# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 22:07:47 2020

@author: mmm
"""

[j+1] = a[j]
            p = p + 1
    print("arrayis sorted in",p,"swaps")
    print("first is:",a[0])
    print("last is:",a[-1])
            
n = int(input())
a = list(map(int, input().rstrip().split()))
p = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j] = a[j + 1]
            a
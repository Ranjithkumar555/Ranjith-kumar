# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 20:39:33 2020

@author: mmm
"""



n = int(input())
a = list(map(int, input().rstrip().split()))
p = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j + 1]:
            a[j] = a[j+ 1]
            a[j + 1] = a[j]
            p =p + 1
    print("array is sorted in", p , "swaps")
    print("First Element :",a[0])
    print("Last Element :",a[-1])
                
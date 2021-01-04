# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:51:34 2021

@author: mmm
"""


def countSwaps(a):
    p = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                a[j] = a[j+ 1]
                a[j + 1] = a[j]
                p =p + 1
    print("array is sorted in", p , "swaps")
    print("First Element :",a[0])
    print("Last Element :",a[-1])
    return a

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))
   
    countSwaps(a)
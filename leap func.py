# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:33:49 2021

@author: mmm
"""


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        return leap
    elif year % 400 == 0:
        return True
           
    return leap

year = int(input())
print(is_leap(year))
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 20:13:39 2021

@author: mmm
"""



import math
import os
import random
import re
import sys


def clt():
     n= int(input())
     if n % 2 == 0 and n < 6 or n > 20 :
        print("Not Weird")
     else:
        print("weird")
if __name__ == '__main__':
    clt()

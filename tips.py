# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:54:28 2021

@author: mmm
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tp =  (meal_cost / 100 ) * tip_percent
    tx = (meal_cost / 100) * tax_percent 
    total = int(round((meal_cost + tp + tx), 0))
    print(total)

   

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())
    
    solve(meal_cost, tip_percent, tax_percent)

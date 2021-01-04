# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:08:59 2021

@author: mmm
"""


from itertools import combinations_with_replacement
s , n = input().split(maxsplit=1)
for i in range(2,int(n)+1):
    for j in combinations_with_replacement(sorted(s),i):
        print(''.join(j))

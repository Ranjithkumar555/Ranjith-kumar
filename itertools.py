# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:01:10 2021

@author: mmm
"""


from itertools import combinations
s , n = input().split(maxsplit=1)
for i in range(1,int(n)+1):
    for j in combinations(sorted(s),i):
        print(''.join(j))

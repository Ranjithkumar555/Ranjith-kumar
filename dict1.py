# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:42:13 2020

@author: mmm
"""


d ={}
for i in range(6):
    d[i] = i*i
print(d)

d = dict()
d = {i : i*i for i in range(6)}
print(d)


d = {"john": 48,"tony": 49,"rahul": 36,"ethi": 39}
ed = {k : v for( k,v) in d.items()  if v % 2 == 0}
print(ed)



original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)



d = {"john": 48,"tony": 49,"rahul": 36,"ethi": 39}
ed = {k : v for( k,v) in d.items()  if v % 2 != 0  and v< 40}
print(ed)




d = {"john": 48,"tony": 49,"rahul": 36,"ethi": 39}
ed = {k : ("old" if v > 40 else "young") for (k,v) in d.items() }
print(ed)

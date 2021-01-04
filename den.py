# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:25:35 2020

@author: mmm
"""


d = {"denis":"den","budaspet":"bud","saigon":"sgn","call":"sgn"}
print(d)
print(d["denis"])
print(d["saigon"])
print(d["call"])
d["temple"] = "temp"
print(d)



d = {"munich":"mun","budapest":"bud","helsinki":"hel"}
for key in d:
    value = d[key]
    print(key +":" + value)
print(d.items())


list = ["hello","hello","world","hello","mars"]
d = {}
for i in list:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)
max_occurences = 0
for key ,value in d.items():
  
    if max_occurences < value:
        max_occurences = value
print(max_occurences)
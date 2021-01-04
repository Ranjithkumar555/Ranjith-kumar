# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 11:42:11 2020

@author: mmm
"""


with open("d:/msc.csv","r") as file:
    for line in file:
        line_split =line.strip().split(";")
        t = line_split[1]
        d = {}
        for Name in t:
            if Name in d:
                d[Name] = d[Name] + 1
            else:
                d[Name] = 1
        print(d)
        
        
        
         
Name = "akash"
count = "11"
Id ="101"        
with open("d:/msc.csv","r") as file:
    for line in file:
        line_split =line.strip().split(";")
        if line_split[1] == Name and line_split[str(3)] == count and line_split[str(0)] == Id :
            print(line_split) 
        
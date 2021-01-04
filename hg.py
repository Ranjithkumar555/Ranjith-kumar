# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:20:50 2021

@author: mmm
"""


arr =[
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]]
 
 
#This function will return the sum of the hourglass
def sum_hg(x, y):
    sum = arr[x][y] + arr[x][y+1] +arr[x][y+2]
    sum = sum + arr[x+1][y+1]
    sum = sum + arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2]
    return sum
 
size = len(arr)
sum = -63
 
for x in range(0, (size-2)):
    for y in range(0, (size-2)):
        k = sum_hg(x, y)
        if k > sum:
            sum = k
 
print("The largest sum of the HourGlass is ", sum)
sum_hg(x,y)
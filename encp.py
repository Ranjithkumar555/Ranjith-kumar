# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:01:35 2020

@author: mmm
"""


class Computer():
    def __init__(self ):
        self._maxprice = 900
    def sell(self):
        print("selling price : {}" .format(self._maxprice))
    def set_maxprice(self,price):
        self._maxprice = price
        
c = Computer()
c.sell()
c._maxprice = 1000
c.sell()
c.set_maxprice(1000)
c.sell()
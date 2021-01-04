# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 18:31:23 2020

@author: mmm
"""


class _Private():
    def __init__(self ,name):
        self.name = name
class Notprivate():
    def __init__(self ,name):
        self.name = name
        self.priv = _Private(name)
        
    def _display(self):
        print("hello")
    def display(self):
        print(" hi ")
test = Notprivate('tim')
test._display()
test.display()


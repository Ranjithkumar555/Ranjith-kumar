# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 20:24:14 2020

@author: mmm
"""


class Maths():
    def nume(self,num):
        self.num = num
        print("enter the number :",num)
        
    def fibbo(self):
        n1 = 1
        n2 = 2
        while(n1 < int(self.num)):
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
    def multi(self):
        sum = 0
        for x in range(0, int(self.num)):
            if( x % 3 ==0 or x % 5 == 0):
                print(" \n ", x)
                sum = sum + x
                continue
        print("sum is : " ,sum)
    def prime(self):
        n = 2
        n3 = int( self.num)
        for i in range(n, int(self.num)):
            if (n > 1):
                for j in range(2 ,i):
                    if(i % j == 0 ):
                        break
                else:
                    print(i)
j = Maths()
j.nume(' 10 ')
j.fibbo()
j.multi()
j.prime() 


                          
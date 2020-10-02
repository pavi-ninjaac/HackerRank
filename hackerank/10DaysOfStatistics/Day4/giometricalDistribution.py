# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 23:13:32 2020

@author: ninjaac
"""


#hackerRank binamial distribution problem
import math

def bi_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

b,b2, p, n = 0,0, 0.12, 10
#probability of no more than 2 rejects
#it can be 0 or 1 or 2
for i in range(0,3):
    b += bi_dist(i, n, p)   
print("%.3f" %b)

#probability of at least 2
#so it can be 2....10
for i in range(2,10):
    b2 += bi_dist(i, n, p)   
print("%.3f" %b2)
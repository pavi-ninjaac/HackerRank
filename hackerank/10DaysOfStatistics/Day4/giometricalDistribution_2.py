# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 23:31:26 2020

@author: ninjaac
"""


#Giometrical distribution
#probablility of succes happening in the 5th chance

def giometricalDistribution(p,n):
    q=1-p
    result=(q**(n-1))*p
    return result

#here the value of p and n is given 
p,n=1/3,5
print('%.3f'%giometricalDistribution(p,n))


#probability of success happing in the first 5 chances

def giometricalDistribution(p,n):
    q=1-p
    result=(q**(n-1))*p
    return result
p,d=1/3,0
for n in range(1,6):
    d+=giometricalDistribution(p,n)
print('%.3f'%d)

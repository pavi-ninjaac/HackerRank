# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 13:42:03 2020

@author: ninjaac
"""



for i in range(1,3+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (int(''.join([str(i) for i in (list(range(1,i+1))+list(range(i-1,0,-1)))])))
    
for i in range(1,3+1):
    print(((10**i - 1)//9)**2)
    """
1
121
12321
"""
###########################################################################################
#divmode
a=int(input())
b=int(input())
print(a//b,a%b,divmod(a,b),sep='\n')

###########################################################################################
#pow and pow()
#pow(a,b,mode) this can be equal to a**b mode m
a=int(input())
b=int(input())
m=int(input())
print(pow(a,b),pow(a,b,m),sep='\n')
###########################################################################################
#read a,b,c,d and print the result of a**b + c**d
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print((a**b)+(c**d))


###########################################################################################
#print the intergers using the arithmatic operations
for i in range(1,3):
    print(i*((10**i)//9))











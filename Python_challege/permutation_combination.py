# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:12:31 2020

@author: ninjaac
"""


#permutation and combination of the given list
x,y,z,n=1,2,3,2
from itertools import permutations
peru=permutations([x,y,z])
result=[]
for i in peru:
    if n !=sum(i):
        result.append(list(i))
        

#combination of the given list
from itertools import combinations 
com=combinations([1,2,3], 2)#2 define how lenthe the result is
for i in com:
    print(i)
    
    
#in the question we are asking to create the permutation along with the 0 
    #so because we are adding the for loop
x,x,y,n=1,2,3,2
result=[]
for x in range(0,x+1):
    for y in range(0,y+1):
        for z in range(0,z+1):
            if (x+y+z)!=n:
                result.append([x,y,z])

#may do it with the single line using the python
print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if (a+b+c)!=n])

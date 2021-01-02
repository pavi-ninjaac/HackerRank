# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:33:34 2021

@author: ninjaac
"""


###################################################################################
# itertools
#find the probability of the 'a' in the given inout
"""
input : 
    4 
    a a c v
    2
    output ;
    0.83333333333334
"""
from itertools import combinations

n = int(input())
p_a , index_of_a=0,[]
letters = input().split()
index = list(range(1,n+1))
iteration = int(input())
combination =list(combinations(index,iteration))

p_s = len(combination)
for index,item in enumerate(letters):
    if item == 'a':
        index_of_a.append(index+1)
        
print(index_of_a)
for i in list(combination):
    print(i)
    make = False
    for j in range(len(i)):
        if i[j] in index_of_a:
            make = True
    if make:
        p_a += 1
        print(p_a)
probability = p_a/ p_s       
print(probability)

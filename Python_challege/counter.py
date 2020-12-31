# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 16:54:35 2020

@author: ninjaac
"""
###################Collections
import collections

################################################################################
#defaultdict

from collections import defaultdict
#it will assign the default value automatically if the key is not defined yet
#it will take a function as default factor and return that if the unknow value is accessed

def default_factor():
    return "Not present in the dict!!"
d = defaultdict(default_factor)
d['a'] = 1
d['b'] = 2
print(d) #defaultdict(<function default_factor at 0x07696CD8>, {'a': 1, 'b': 2})

#which is not present 
print(d['C']) #Not present in the dict!!

################################################################################
#defaultdict
# creating default with list

d=defaultdict(list)
n,m = map(int,input().split())
for i in range(n+m):
    d[input()].append(i)
print(d)

################################################################################
#defaultdict
from collections import defaultdict
d = defaultdict(list)
list1=[]

n, m = map(int,input().split())

for i in range(0,n):
    d[input()].append(i+1) 

for i in range(0,m):
    list1=list1+[input()]  

for i in list1: 
    if i in d:
        print(" ".join( map(str,d[i]) ))
    else:
        print -1
        

################################################################################
#defaultdict        

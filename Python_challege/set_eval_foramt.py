# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:44:20 2020

@author: ninjaac
"""

import cmath
print(*cmath.polar(complex(input())),sep='\n')

###################################################################################
#Introdunction to set
a = set(map(int,input().split()))
print(sum(a)/len(a))

###################################################################################
#set add function

n , s= int(input()),set()
for i in range(n):
    
    s.add(input())
print(len(s))

###################################################################################
#set delete functions
# pop,remove(4),discard(4)
"""
n=input()
s=set(input().split())
f = int(input())
for i in range(f):
    statemetn = input().split()
    if statemetn[0] == "pop":
        s.pop()
        print(s)
    elif statemetn[0] == 'remove':
        s.remove(statemetn[1])
        print(s)
    else:
        s.discard(statemetn[1])
        print(s)
print(s)

"""
#this can be shorteb using the eval and formate methids
n=input()
s=set(input().split())
f = int(input())
for i in range(f):
    eval('s.{0}[{1}]'.format(*input().spilt()+['']))
print(sum(s))

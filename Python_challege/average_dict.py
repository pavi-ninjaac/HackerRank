# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:36:01 2020

@author: ninjaac
"""

n=int(input())
dictt=dict()
for _ in range(n):
    d=input().split(' ')
    dictt[d[0]]=[float(a) for a in d[1:]]
q=input()
print("%.2f"%(sum(dictt[q])/3))


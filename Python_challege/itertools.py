# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:20:58 2021

@author: ninjaac
"""


"""
Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output

206
Explanation

Picking 5 from the 1st list,  9from the 2nd list and 10 from the 3rd list gives the maximum  value 
#(5**2,9**2,10**2) % 1000=206.
"""

k,m = map(int,input().split())
l=[]
for i in range(k):
    l.append(max(map(int,input().split())))
    
print((sum([i**2 for i in l]))%m)

"""
from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))
"""
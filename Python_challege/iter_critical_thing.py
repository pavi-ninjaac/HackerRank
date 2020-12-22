def func(a,*b):
    print(a,b)
    
func(1,2,3,4)# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 13:54:49 2020

@author: ninjaac
"""

def print_formatted(number):
    # your code goes here
    width=len(bin(n)[2:])
    for i in range(1,n+1):
        for form in 'doXb':
            print('{0:{width}{base}}'.format(i,base=form,width=width),end=' ')
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
    
    
###################################################################################
from itertools import product
A = map(int,input().split())
B = map(int,input().split())
product =list( product(A,B))
print(*product)     

###################################################################################

from itertools import permutations
s,r = input().split()
print(*[''.join(a) for a in list(permutations(sorted(s),int(r)))],sep = '\n')
###################################################################################

print('{0:{fill}{align}33}'.format(3,fill = '|',align='^'))

###################################################################################



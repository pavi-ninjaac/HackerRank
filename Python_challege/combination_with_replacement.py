# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:04:27 2021

@author: ninjaac
"""


###################################################################################
# itertools
from itertools import combinations_with_replacement,combinations
print(list(combinations('12345',2)))
print(list(combinations_with_replacement('12345',2)))

"""
Sample Input

HACK 2
Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
"""
t,r = input().split()
print(*[''.join(a) for a in list(combinations_with_replacement(sorted(t), int(r)))],sep='\n')

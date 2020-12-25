# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:22:37 2020

@author: ninjaac
"""


#############################################################################################

#Array manupulation

"""def matchingStrings(s, q):
    for query in q:
        lenth = 0
        for strings in s:
            if query == strings:
                lenth +=1
        print(lenth)"""
        
# this can be shorten as
def matchingStrings(s,q):

    a = [1 if query == string else 0 for query in q for string in s ]
    print(a)
    print(*[sum(a[i:i+len(s)]) for i in range(0,len(a),len(s)+1)],sep='\n')   
matchingStrings(['aba', 'baba', 'aba', 'xzxb'],['aba', 'xzxb', 'ab'])

###################################################################################

import numpy as np

a = np.zeros(10,dtype = 'int')
q=[[1,5,3],[4,8,7],[6,9,1]]
for i,j,k in q:
    a[i-1:j] = a[i-1:j] +k
print( a.max())


























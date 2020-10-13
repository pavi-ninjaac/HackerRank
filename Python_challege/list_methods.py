# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:58:38 2020

@author: ninjaac
"""

if __name__=='__main__':
    t=int(input())
    result=[]
    for _ in range(t):
        a=list(input().split())
    
        if a[0]=='insert':
            result.insert(int(a[1]),int(a[2]))
        elif a[0]=='print':
            print(result)
        elif a[0]=='remove':
            result.remove(int(a[1]))
        elif a[0]=='append':
            result.append(int(a[1]))
        elif a[0]=='sort':
            result.sort()
        elif a[0]=='pop':
            result.pop()
        elif a[0]=='reverse':
            result=result[::-1]

l=[(1,2),(3,1)]
sorted(l,key=lambda x: x[1],reverse=True)    
print(l)
        
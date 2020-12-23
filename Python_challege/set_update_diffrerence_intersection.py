# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:49:05 2020

@author: ninjaac
"""
###################################################################################

#set intersection function

n= input()
A = set(input().split())
b = input()
B = set(input().split())
print(len(A.intersection(B)))
print(len(A & B))

print(set("Pavithra").intersection('Rank'))
print(set("Pavithra").intersection(['Rank']))
print(set("Pavithra").intersection({"pavi":1}))

###################################################################################

#set difference function

n= input()
A = set(input().split())
b = input()
B = set(input().split())
print(len(A.difference(B)))

print(len(A - B))

print(set("Pavithra").difference('Rank'))
print(set("Pavithra").difference(['Rank']))
print(set("Pavithra").difference({"pavi":1}))

###################################################################################

#set symatric_difference function
# semmatic difference will return the element in the both list but not in the both ,, except 
#internsection
# Enter your code here. Read input from STDIN. Print output to STDOUT

n= input()
A = set(input().split())
b = input()
B = set(input().split())
print(len(A.symmetric_difference(B)))

print(A ^ B)

print(set("Pavithra").symmetric_difference('Rank'))
print(set("Pavithra").symmetric_difference(['Rank']))
print(set("Pavithra").symmetric_difference({"pavi":1}))

###################################################################################

s=set([1,2,3,4,5,6,7,8])
getattr(s,'update')([1,2,3]) # this is equal to s.update([1,2,3,4]) use of getattr
print(s)








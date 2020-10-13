# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:12:58 2020

@author: ninjaac
"""

#############using the formate function
def print_full_name(a, b):
    print("Hello {a} {b} ! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name) 
    
    

####### change the string using the list

def mutate_string(string, position, character):
    a=list(string)
    a.insert(position,character)
    a.pop(position+1)
    return ''.join(a)
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:42:59 2020

@author: ninjaac
"""


"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
"""
def swap_case(s):
    a=[]
    for ch in s:
        if ch.islower():
            a.append(ch.upper())
        else: a.append(ch.lower())
    
    #single line
    print(''.join([ch.upper() if ch.islower() else ch.lower() for ch in s]))
    return ''.join(a)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


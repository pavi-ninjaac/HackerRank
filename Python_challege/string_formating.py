# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:55:18 2020

@author: ninjaac
"""
"""
Given an integer,n , print the following values for each integer  from 1 to n :

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of .
"""

def print_formatted(number):
    # your code goes here
    w=len(bin(number)[2:])
    for i in range(1,n+1):
        print (str(i).rjust(w,' '),oct(i)[2:].rjust(w,' '),hex(i)[2:].rjust(w,' '),bin(i)[2:].rjust(w,' '))    

        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
i=3
w=2
print (str(i).rjust(w,' '),oct(i)[2:].rjust(w,' '),hex(i)[2:].rjust(w,' '),bin(i)[2:].rjust(w,' '))    
print('%d'%2)
print(bin(2))
print('%O'%2)
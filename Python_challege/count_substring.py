# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:04:26 2020

@author: ninjaac
"""

def count_substring(string, sub_string):
    return string.count(sub_string)
    #return (''.join(string)).count(''.join(sub_string))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

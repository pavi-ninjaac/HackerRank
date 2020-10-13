# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:13:35 2020

@author: ninjaac
"""


"""
Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
"""

#find the substring
def count_substring(string, sub_string):
    """
    count=0
    for i in range(0,len(string)):
        print(string[i:i+len(sub_string)])
        if string[i:i+len(sub_string)]==sub_string:
            count+=1
    """
    #chnage this to one line
    return sum([1 for i in range(0,len(string)) if string[i:i+len(sub_string)]==sub_string])
    #return count
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
    






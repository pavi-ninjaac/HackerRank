# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 17:18:40 2020

@author: ninjaac
"""


'''
Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
'''
from collections import Counter
l=[]
for i in range(int(input())):
    l.append(input())
print(*Counter(l).values())

###################################################################################
# count the things in a word



from collections import Counter

chars = Counter(input()).items()

for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
    print(char, n)

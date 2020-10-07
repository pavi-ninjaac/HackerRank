# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:20:38 2020

@author: ninjaac
"""
"""
In this challenge, we practice using linear regression techniques. Check out the Tutorial 
tab for learning materials!

Task
A group of five students enrolls in Statistics immediately after taking a Math aptitude test. 
Each student's Math aptitude test score, x, and Statistics course grade,y , can be expressed as 
the following list of  points:
    
If a student scored an 80  on the Math aptitude test, what grade would we expect them to 
achieve in Statistics? Determine the equation of the best-fit line using the least squares
 method, then compute and print the value of Y
"""
#### find the corrilation coefficient
n = 5
xy = [map(int, input().split()) for _ in range(n)]
sx, sy, sx2, sxy = map(sum, zip(*[(x, y, x**2, x * y) for x, y in xy]))
b = (n * sxy - sx * sy) / (n * sx2 - sx**2)
a = (sy / n) - b * (sx / n)
print('{:.3f}'.format(a + b * 80))
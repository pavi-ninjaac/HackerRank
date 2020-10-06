# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:08:16 2020

@author: ninjaac
"""

#poision distribution


import math
def poision_D(k,lamp):
    return (lamp**k)*(math.exp(-lamp))/math.factorial(k)

result=poision_D(5,2.5)
print('%.3f'%result)

#poision challeng 2
averageX, averageY = [float(num) for num in input().split(" ")]

# Cost
CostX = 160 + 40*(averageX + averageX**2)
CostY = 128 + 40*(averageY + averageY**2)

print(round(CostX, 3))
print(round(CostY, 3))
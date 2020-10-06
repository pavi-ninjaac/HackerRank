# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:32:43 2020

@author: ninjaac
"""


import math
mean, std = 20, 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print('{:.3f}'.format(cdf(19.5)))
# Between 20 and 22
print('{:.3f}'.format(cdf(22) - cdf(20)))


#challengw 2
import math

mean, std = 70, 10
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

#grade >80
print('{:.2f}'.format((1 - cdf(80))* 100))
#grade >=60
print('{:.2f}'.format((1- cdf(60))* 100))
#grade <60
print('{:.2f}'.format(cdf(60)*100))
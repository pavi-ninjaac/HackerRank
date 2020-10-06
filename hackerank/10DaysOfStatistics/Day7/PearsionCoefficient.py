# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:24:13 2020

@author: ninjaac
"""


"""
Objective
In this challenge, we practice calculating the Pearson correlation coefficient. Check out the Tutorial tab for learning materials!

Task
Given two n-element data sets, X and Y , calculate the value of the Pearson correlation coefficient.
"""
import numpy as np
n=int(input("enter the size"))
X=input().split()
Y=input().split()

X=np.array(X).astype('float64')
Y=np.array(Y).astype('float64')
x_mean=np.mean(X)
x_sd=np.std(X)

y_mean=np.mean(Y)
y_sd=np.std(Y)

mean_sum=0
for i in range(0,int(n)):
    mean_sum+=(X[i]-x_mean)*(Y[i]-y_mean)

coefficient=mean_sum/(n*x_sd*y_sd)
print('%.3f'%coefficient)   

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:52:19 2020

@author: ninjaac
"""
"""
Basically, the central limit theorem says, if  is a random variable that belongs to any 
distribution with mean  and standard deviation , then the sum of these random variables 
will converge to a normal distribution (provided n is big enough) with mean  and standard 
deviation .
We can calculate the parameters of this normal distribution and find the cumulative 
"""
import math

x = 
n = 
mu = 
sigma = 

mu_sum = n * mu 
sigma_sum = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(x, mu_sum, sigma_sum), 4))

#### chalenge 2
"""
The number of tickets purchased by each student for the University X vs. 
University Y football game follows a distribution that has a mean of(sample mean) 2.4  and 
a (sample sd)standard deviation of 2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets.
 If there are only 250 tickets left, what is the probability that all 100 students will be able 
 to purchase tickets?
"""
import math
x = 250
n = 100
mu = 2.4
sigma = 2.0

mu_sum = n * mu 
sigma_sum = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(x, mu_sum, sigma_sum), 4))



########### chalenge 2
import math
x = 250
n = 100
mu = 2.4
sigma = 2.0

mu_sum = n * mu 
sigma_sum = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(x, mu_sum, sigma_sum), 4))



############# chalenge 3
samples = 100
mean = 500
sd = 80
interval =0.95 
z = 0.5

sd_sample = sd / (samples**0.5)
print(round(mean - sd_sample*z,2))
print(round(mean + sd_sample*z,2))
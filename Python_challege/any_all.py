# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:56:23 2020

@author: ninjaac
"""


"""
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .
"""



s='aQ2'
for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in s))
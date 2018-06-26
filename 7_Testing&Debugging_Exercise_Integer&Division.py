#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 06:28:00 2018

@author: tuheenahmmed
"""

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    while x >= a:
        count += 1
        x = x - a
    return count

'''
When we call

print(integerDivision(5, 3))
we get the following error message:

File "temp.py", line 9, in integerDivision
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment

'''


#debugging solution



def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

print(integerDivision(5,3))
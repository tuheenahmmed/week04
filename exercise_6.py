#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 07:04:44 2018

@author: tuheenahmmed
"""

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        rem(x-a, a)


rem(7, 5)

#no output




#debugging solution


def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        #print('helen')
        return rem(x-a, a)
        

rem(11, 5)

rem(2, 5)
the shell returns 2. When we call

rem(5, 5)
the shell returns 0. But when we call


'''
Explanation:

In the conditional, the final clause contains a recursive call that we never return the results of! 
Thus the final line - rem(x-a, a) - simply needs to be modified such that we return its value. Easy enough! 
The solution is thus return rem(x-a, a) 
 
'''
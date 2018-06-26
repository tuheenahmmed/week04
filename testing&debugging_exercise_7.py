#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 07:39:10 2018

@author: tuheenahmmed
"""

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)

  
f(3)


#solution

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)

  
f(5)


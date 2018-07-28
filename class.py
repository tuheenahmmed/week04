#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 07:11:22 2018

@author: tuheenahmmed
"""

'''
A blueprint for a house design is like a class description. 
All the houses built from that blueprint are objects of that class. 
A given house is an instance.
'''

class House(object):
    def _init_(self,street,rooms,bathrooms):
        self.street = 35
        self.rooms = 15
        self.bathrooms = 16
        self.clean = True
        
    
    def dcleenHouse(self):
        if not self.clean:
            self.clean = True
            print ("helens pudanda is not clean")
            
        else:
            print ("cheers pudana is fuckable")
            
    
    def unCleanHouse (self):
        if self.clean:
            self.clean =False
            print ("Jasmines pudanda is young and tight and juicy")
            
        else:
            print ("I want to fuck Jasmine")
            
    def talk (self, phrase):
        print (phrase)
        
        
###################
        
class Cls(object):
    def __init__(self, x):
        self.x = x

    def Mth(self):
        x = 5
        y = x * 2
        print(self.x, x, y)

Ins = Cls(2)
Ins.Mth()     


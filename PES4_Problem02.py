#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 07:52:56 2018

@author: tuheenahmmed
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    
    newhand=hand.copy()
    #print(newhand)
    
    for letter in word:
        if letter in hand:
            newhand[letter]=newhand[letter]-1
            #print(newhand)
    return newhand
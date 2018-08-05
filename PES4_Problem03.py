#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 07:53:31 2018

@author: tuheenahmmed
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    #newhand = getFrequencyDict(word).copy()
    newhand = hand.copy()
    
    if word not in wordList:
        return False
    
    #compare letters in word and hand and check if it is equal or not
    for letter in word:
        
        if letter not in hand:
            return False
        
        else:

            newhand[letter]=newhand[letter]-1
            if newhand[letter] <0:
                return False
            
    return True
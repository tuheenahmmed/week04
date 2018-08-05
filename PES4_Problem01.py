#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 07:51:51 2018

@author: tuheenahmmed
"""

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
#    values=SCRABBLE_LETTER_VALUES.values()
#    keys=SCRABBLE_LETTER_VALUES.keys()
    
    score =0
    if word == []:
        return score 
        
    else:
            
        for letter in word:
            if letter in SCRABBLE_LETTER_VALUES:
                #print (letter)
                score1=SCRABBLE_LETTER_VALUES[letter]
                #print(score1)
                score=score+score1
                #print(score)
        score=score*len(word)
        #print(score)
        
        
        if len(word) == n:
            score = score+50
            
            return score
 
        return score
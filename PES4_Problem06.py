#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 07:55:59 2018

@author: tuheenahmmed
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """

    StoreHand={}
    
    
    while True:
        
        userInput = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        
        if userInput=='e':
            
            break
        
        elif userInput=='n':
            
            hand=dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            StoreHand= hand
            continue
        
        elif userInput=='r' and StoreHand=={}:
            
            print("You have not played a hand yet. Please play a new hand first!")
            continue
        
        elif userInput=='r':
                playHand(hand, wordList, HAND_SIZE)     
            
        else:
            
            if userInput!='n' or 'r' or 'e':
            
                print("Invalid command.")
                continue
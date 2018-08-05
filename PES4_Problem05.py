#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 07:54:55 2018

@author: tuheenahmmed
"""

def playHand(hand, wordList, n):

    # Keep track of the total score
    FinalScore=0
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is a single period:
        
            # End the game (break out of the loop)


    while calculateHandlen(hand) !=0:
    
        print("Current Hand: ", end="")
        #displayHand(hand)
        displayHand(hand)
        userInput = input("Enter word, or a " '"'  "." '"' " to indicate that you are finished: ")
        
        if userInput == '.':
            
            break

        
        # Otherwise (the input is not a single period):
        
            # If the word is not valid:
            
                # Reject invalid word (print a message followed by a blank line)
                
        else:
            
            if isValidWord(userInput, hand, wordList)==False:
            #if userInput not in wordList:
              print("Invalid word, please try again.")
              print("")
              continue


            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand 
                
            
            else:
            
                TotalScore= getWordScore(userInput, n)
                FinalScore+=TotalScore
                print('"' +userInput+ '"' ,"earned",TotalScore,"points.","Total:",FinalScore,"points" )
                print("")

        hand=updateHand(hand,userInput)        
        
        
           
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand)==0:       
        print("Run out of letters. Total score:",FinalScore, "points.")
    
    else:
        print("Goodbye! Total score: ",FinalScore, "points.")
 
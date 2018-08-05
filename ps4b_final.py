#from ps4a import *
#import time

# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "/Users/tuheenahmmed/documents/python/week04/ProblemSet4/words.txt"
#WORDLIST_FILENAME = "C:/Users/etuhahm/Desktop/Python_guni/week04/ProblemSet4/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList



def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
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
    
#getWordScore("pudand", 6) 



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line


#displayHand({'a':1, 'x':2, 'l':3, 'e':1})

#dict={'a':1, 'x':2, 'l':3, 'e':1}


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
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

#hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1} 
    
#updateHand({'l': 2, 'm': 1, 'i': 1, 'u': 1, 'q': 1, 'a': 1}, 'quail')


#updateHand({'a':1, 'x':2, 'l':3, 'e':1},"l")



#
# Problem #3: Test word validity
#

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
    
#isValidWord("axxllle", {'a':1, 'x':2, 'l':3, 'e':1}, "axxllle" )
#isValidWord("teeth", {'s': 1, 'e': 2, 'b': 2, 'h': 2, 't': 2},"teeth")
#isValidWord("milk", {'i': 2, 'd': 1, 'h': 1, 'y': 1, 'm': 1, 'l': 1, 'k': 1}, "milk")
#isValidWord("tea", {'m': 1, 'e': 1, 't': 2, 'a': 1, 'u': 2, 'c': 1, 'r': 1, 'p': 2, 's': 1}, "tea")

#isValidWord('hello', {'h': 1, 'e': 1, 'l': 2, 'o': 1}, "hello")


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    length =0
    for letter in hand:
       length += hand[letter]
       
    return length

#calculateHandlen({'h': 1, 'e': 1, 'l': 2, 'o': 0})


#
#Problem #5: playing a Hand

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
       



#wordList = loadWords()
#playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)

    
#wordList = ["","him","cam","","","big","tow","fast"]
#playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
#playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
#playHand({'a': 1, 'e': 1, 'l': 1, 'p': 1, 'r': 1, 's': 1, 't': 2, 'u': 1, 'z': 1},wordList,10)





#
# Problem #6: Playing a game
# 
'''
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
            
#playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
'''            
            
#
# Build data structures used for entire session and play game
#


#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

#compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)



#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

    
#
# Problem #7: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """



    StoreHand={}
    
    
    while True:
        
        userInput = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        #userInput1= input("Enter u to have yourself play, c to have the computer play: ")
        
        if userInput=='e':
            
                break
            
        elif userInput=='r' and StoreHand=={}:
            
                print("You have not played a hand yet. Please play a new hand first!")
                continue
        
        #userInput1= input("Enter u to have yourself play, c to have the computer play: ")
        
        elif userInput=='n':
            
            while True:
                userInput1= input("Enter u to have yourself play, c to have the computer play: ")
                
                if userInput1=='u':
            
                    hand=dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    StoreHand= hand
                    break
        
                elif userInput1=='c':
                
                    hand=dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    StoreHand= hand
                    break
            
                else:
                    print("Invalid command.")
                    continue
            
        
        elif userInput=='r':
            
            while True:
                userInput1= input("Enter u to have yourself play, c to have the computer play: ")
            
                if userInput1=='u':
                
                    playHand(hand, wordList, HAND_SIZE)  
                    break
                
                elif userInput1=='c':
                
                    compPlayHand(hand, wordList, HAND_SIZE) 
                    break
                        
                else:
                    print("Invalid command.")
                    continue
            
        else:
            
            if userInput !='n' or 'r' or 'e':
            
                print("Invalid command.")
                continue

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)



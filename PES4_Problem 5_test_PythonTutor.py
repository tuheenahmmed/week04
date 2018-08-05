SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def updateHand(hand, word):

    newhand=hand.copy()

    for letter in word:
        if letter in hand:
            #newhand[letter]=newhand[letter]-1
            newhand[letter]-=1
    return newhand
    
def displayHand(hand):

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

def getWordScore(word, n):
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

def calculateHandlen(hand):

    length =0
    for letter in hand:
       length += hand[letter]
       
    return length



def isValidWord(word, hand, wordList):

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
    
def playHand(hand, wordList, n):

    # Keep track of the total score
    FinalScore=0
    

    while calculateHandlen(hand) !=0:
    
        print("Current Hand: ", end="")
        #displayHand(hand)
        displayHand(hand)
        userInput = input("Enter word, or a " '"'  "." '"' " to indicate that you are finished: ")
        
        if userInput == '.':
            
            break


        else:
            
            #if userInput not in wordList:
            if isValidWord(userInput, hand, wordList)==False:
              print("Invalid word, please try again.")
              print("")
              continue

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
    
    
wordList = ["","him","cam","","","big","tow","fast"]
#playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
#playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
playHand({'a': 1, 'e': 1, 'l': 1, 'p': 1, 'r': 1, 's': 1, 't': 2, 'u': 1, 'z': 1},wordList,10)
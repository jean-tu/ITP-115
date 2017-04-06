# Jean Tu
# ITP 115, Spring 2017
# Assignment 4: Word Jumbled and encryption
# 02/12/2017
# Description
#   This is the word jumbled w/ extra credit

import random

wordList = ["random", "green", "roller", "sandwich", "boba", "pancake", "chocolate"]
hintList = ["not something in order", "a color", " ___ blades", "ice cream ____ ", "a hipster drink",
            "___ and eggs and bacon for a hearty breakfast", "a girl's weakness"]

#will display the hint if the user is stuck and wants one
def displayHint(index):
    print(hintList[index])

def checkWord(word, index):
    if word.lower() == wordList[index]:
        return True
    else:
        return False


def main():
    #Choose a random word from wordList
    guess = 1   # to keep track of the number of guesses the user has made
    lengthOfWordList = len(wordList)
#    print(lengthOfWordList)
    index = random.randrange(0, lengthOfWordList)
    randomWord = wordList[index]
    randomWord = ''.join(random.sample(randomWord, len(randomWord))) #to randomize the characters of the string
    print("The jumbled word is \"" + randomWord + "\"")
    stillGuess = True #while the person still hasn't gotten it right yet
    while stillGuess == True:
        print()
        guessWord = input("Please enter your guess: ")
        if checkWord(guessWord, index) == False:   # if the user guessed wrong
            hint = input("Try again.... Would you like a hint? (y/n): ")
            if hint.lower() == "y":
                displayHint(index)
            #else, do nothing and continue
            guess += 1  #adding one on for guessing wrong
        else: #if the person got the guess right
            stillGuess = False  #jump out of the while loop because they got the guess
    #end of while loop
    print()
    if(guess == 1):
        print("You got it! \nIt took you", str(guess), "try.")
    else:
        print("You got it! \nIt took you", str(guess), "tries.")

main() #calling on the main function

# Jean Tu
# ITP 115, Spring 2017
# Assignment 2: Vending Machine & Choose Your Own Adventure Game
# 02/05/2017
# Description:
#   Pig Latin Assignment for part 1
#   Extra Credit for the Elvish Pig Latin & Commented answers below
#

#Part 1 ------------------------------------------------------------------------------------------
import random # to be able to do the EC

print("Elcómewó óten heten Igpén Lvísheá ránslátórtë! \n(Welcome to the Pig Elvish translator!)")
print()

vowels = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

translate = True

while translate == True:
    toTranslate = input("Please enter a word you would like to translate: ")
    #Doing the translation English --> Elvish
    wordLength = len(toTranslate)
    elvish = toTranslate[1:wordLength] + toTranslate[0]
    elvish = elvish.lower() # make sure that the whole word is in lower case
    elvish = elvish[0].upper() + elvish[1:len(elvish)]
    if(len(elvish) <= 3): #if the word is less than or equal to 3
        #append -en to the end
        toAppend = "en"
        elvish = elvish + toAppend
    elif(len(toTranslate) >= 4): # if the word is 4 characters or more, append a vowel
        elvish = elvish + random.choice(vowels) #appending a random vowel

    # Changing all of the 'k' to 'c'
    elvishCopy = elvish
    elvish = "" # to erase it to be able to use it again
    for letter in range(len(elvishCopy)):
        #print()
        if (elvishCopy[letter] == "k"):
            elvish += "c"
        else:
            elvish = elvish +  elvishCopy[letter]

    if(elvish[len(elvish)-1] == "e"): #if the last character is e
        #Count how many "e"'s there are
        eCount = 0
        for letter in elvish:
            if(letter == "e"):
                eCount += 1

        print("E count: " , str(eCount))
        elvishCopy = elvish
        elvish = "" #reset to be able to use again
        for i in elvishCopy:
            if (i == "e"):
                if (eCount == 1):
                    elvish += "ë"   #if there is 1 left and it is the last one
                elif (i == "e"):
                    elvish += i
                    eCount -= 1 #remove 1 from the count
            else:
                elvish += i #is just a regular character
    print("'"+toTranslate + "' in elvish is", elvish)
    anotherWord = input("Would you like to translate another word?(y/n): ")
    if anotherWord.lower() == "n":
        translate = False
    # else it will remain true and loop back to the beginning
print()
print("Oodbyega! Aveha aen icenë ayden!\n(Goodbye! Have a nice day!)")

print()
print("===========Extra Credit=============")
yesNo = input("Would you like to convert a word from PigLatin to English? (y/n): ")
if yesNo.lower() == "y":
    pigtoEngl = True
else:
    pigtoEngl = False
while pigtoEngl == True:
    word = input("Enter the word you would like to convert to English: ")
    word = word.lower()
    wordLength = len(word)
    if (word[wordLength-2] == "e") and (word[wordLength-1]=="n"): #then it was a 3 letter word or less
        word = word[0:wordLength-2]
    else: #word was 4 or more
        word = word[0:wordLength-1] #remove the last added word (would be the added vowel)
        word = word[len(word)-1] + word[0:len(word)-1]

    print("The word you entered was: ", word)
    print()
    yesNo = input("Would you like to convert another word? (y/n): ")
    if yesNo.lower() == "n":
        pigtoEngl = False
    #else: It stays at true and will continue in the loop

"""
Extra Credit response
It's hard to actually know if you got the original version of the word. You can try
what you can to revers it, but you run into the issue of was it a three letter word
or less? Since you have to add an "-en" at the end of it. You can create a parse to
look for that, but it is harder especially since we have the random generator to
choose a random vowel to enter and switch the k's to c's and the ë.
"""




#Part 2 ------------------------------------------------------------------------------------------
print()
print("=========LARGEST NUMBER=============")
toContinue = True
while toContinue == True:   #while the user wants to play another round
    largestNumber = 0
    print("Input an integer greater or equal to 0 or -1 to quit: ")
    inputNum = 1 #just a default
    while (inputNum != -1):
        inputNum = int(input("> "))
        if (inputNum > largestNumber):
            largestNumber = inputNum
        #else:
            #Do nothing and carry on to the next input number
    print("The largest number is: ", str(largestNumber))
    print()
    cont = input("Would you like to find the largest number again? (y/n): ")
    if (cont.lower() == "n"): #they want to stop
        toContinue = False # set it to break out of the loop
print()
print("Goodbye!")


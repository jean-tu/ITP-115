# Jean Tu
# ITP 115, Spring 2017
# Lab L6
# jeantu@usc.edu

# Word manipulation

def strip(word):
    word = word.lower() #converting the word to all lower case
    word = word.replace(" ", "")  #stripping the word of the spaces
    return word #return the word that has been stripped

#Checks if the two words are anagrams of each other, if they are then T; else F
def anagram(word1, word2):
    for i in word1:
        if word2.find(i) == -1: #if the letter is not in the other word
            return False #then it is not an anagram
    return True

#checks to see if the two words are palindromes of each other
def palindrome(word):
    wordLen = len(word)-1
    for i in word:
        if (i != word[wordLen]):
            return False
        wordLen = wordLen -1
    return True

#calls on each of the previously defined functions
def main():
    word1 = input("Please enter a word or statement: ")
    word2 = input("Please enter a second word or statement: ")
    word1 = strip(word1)
    word2 = strip(word2)
    if anagram(word1, word2) == True:
        print("The two words you entered are anagrams")
    else:
        print("The two words you entered are NOT anagrams")
    if palindrome(word1) == True:
        print("The first word is a palindrome")
    else:
        print("The first word is not a palindrome")
    if palindrome(word2) == True:
        print("The second word is a palindrome")
    else:
        print("The second word is not a palindrome")


main()
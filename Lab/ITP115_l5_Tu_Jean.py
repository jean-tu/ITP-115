# Jean Tu
# ITP 115, Spring 2017
# Lab L5
# jeantu@usc.edu

import random

articles = ["the", "a", "it", "that"]
nouns = ["house", "car", "person", "milk"]
verbs = ["quiet down", "leap", "walked", "ran"]

choice = 0
print("welcome to the Sentence Generator")
while choice != 5:
    print(" Menu")
    print(" 1) View Words")
    print(" 2) Add Words")
    print(" 3) Remove Words")
    print(" 4) Generate Sentence")
    print(" 5) Exit")
    choice = int(input("> "))
    if choice == 1:     #view words
        print("articles:", articles)
        print("nouns:", nouns)
        print("verbs:", verbs)
    elif choice == 2:   #add words
        listType = int(input("Enter 1) for nouns 2) for verbs: "))
        if listType == 1:
            word = input("Enter the Noun: ")
            nouns.append(word)
        elif listType == 2:
            word = input("Enter the Verb: ")
            verbs.append(word)
        else:
            print("ERROR: Invalid option")
    elif choice == 3:   #remove words
        found = False
        listType = int(input("Enter 1) for nouns 2) for verbs: "))
        if listType == 1:
            word = input("Enter the Noun: ")
            #have to check if the word exists
            for x in nouns:
                if x == word:
                    nouns.remove(word) #the word exists, so remove it
                    found = True
            if found == False:
                print(word, "not in list")
        elif listType == 2:
            word = input("Enter the Verb: ")
            #checking if the word exists
            for v in verbs:
                if v == word:
                    verbs.remove(word)
                    found = True
            if found == False:
                print(word, "not in list")
        else:
            print("ERROR: Invalid option")
    elif choice == 4:   #generate sentence
        print(random.choice(articles), random.choice(nouns),
              random.choice(verbs), random.choice(articles),
              random.choice(nouns))
    elif choice == 5:
        print("Program will exit \nHave a great day!")
    else:
        print("ERROR: Invalid choice")

    print()
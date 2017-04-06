# Jean Tu
# ITP 115, Spring 2017
# Lab L11 - Dictionaries
# jeantu@usc.edu

def main():
    fileName = input("What file do you want to open? ")
    file = open(fileName, "r")
    letterFreq = {}

    for line in file:
        line = line.strip()
        for letter in line:
            if letter not in ",-:;\" .'—":
                if letter.lower() not in letterFreq: #it it doesn't exit
                    letterFreq[letter.lower()] = 1 #add the letter to the dictionary as key & value = 1
                else: # else the letter exists
                    letterFreq[letter.lower()] += 1# add one to the current
    file.close()

    listKey = list(letterFreq.keys()) #turn the keys from the dictionary into a list
    listKey.sort() #sort the keys
    for key in listKey:
        print(key, "appears", letterFreq[key], "times")

main()
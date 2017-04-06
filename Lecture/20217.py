# import random
# bands = ["paramour", "maroon 5", "jonas brothers", "the beatles", "radiohead"]
#
# print("Here are the bands listed: ")
# for band in bands:
#     print(band, end=",")
#
# print()
# name = input("Enter a band to remove: ")
# if name.lower in bands: #check to see if what the user entered is in the list
#     bands.remove(name.lower())
# else:
#     print("Oops! Could not find", name)
#
# bands.sort()
# ranNumber = random.randint(0,len(bands)-1)
# del bands[ranNumber]
#
#
# print("Here are the bands listed: ")
# for band in bands:
#     print(band, end=",")


# ##NEXT
# wordList = ["Always", "look", "on", "the", "bright", "Side" , "of", "life"]
# delimiter = " "
# quote = delimiter.join(wordList)
# print(quote)
#
# quote = "spam-spam-spam"
# delimiter = "-"
# wordList = quote.split(delimiter)
# print(wordList)

#NEXT
msg = "to be or not to be"
#Goal: make a list, then lets make a list without repeated items
delimiter = " "
wordList = msg.split(delimiter)

trimmedWordList = []
for word in wordList:
    if word not in trimmedWordList:
        trimmedWordList.append(word)

print(wordList)
trimmedMsg = " ".join(trimmedWordList)
print(trimmedMsg)

letterList = list(trimmedMsg) #chopps the whole thing
while "o" in letterList:
    letterList.remove("o")
finalMsg = "".join(letterList)
print(letterList)
print(finalMsg)









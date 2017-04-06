
# def main():
#     msg = "to be or not to be"
#     wordList = msg.split(" ")
#     print(wordList)
#
#     # make a dictionary that counts how many times a word appears in the string
#     wordFrequency = {}
#     for word in wordList:
#         if word in wordFrequency:
#             wordFrequency[word] += 1
#         else:
#             wordFrequency[word] = 1
#
#     for key in wordFrequency:
#         print("the word \"" + key + "\" appears", wordFrequency[key])
#
#
# main()

#-----------------------------


def main():
    favorites = {}
    favorites["beverage"] = "root beer"

    favorites["food"] = [] #is an empty list
    favorites["food"].append("Cookies") #adding to the list
    favorites["food"].append("pizza")


    favorites["music"] = "hip hop"

    #want it to be printed in alphabetical order
    keyList = list(favorites.keys()) #returns a list of all the keys
    keyList.sort()



    for key in keyList:
        print("favorite", key, ":", favorites[key])

main()
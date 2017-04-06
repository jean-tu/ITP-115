# Review

"""
1) You can iterate through different things using a for loop: list, strings, range, dictionary, and files (read 1 line @ a time)
"""

# function name: countItems
# description: count the number of times an item appears
# input:
#   itemToCheck is a single element
#   listOfItems is a list of elements
# output/ return:
#   Returns an int representing the number of items itemToCheck appears in the list
def countItems(itemToCheck, listOfItems):
    counter = 0
    for element in listOfItems:
        if element == itemToCheck:
            counter += 1
    return counter


def main():
    listOfItems = ["apple", "pear", "apple"]
    count = countItems("apple", listOfItems)
    print(count)

main()
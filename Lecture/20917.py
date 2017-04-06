
import random

#Constants
COIN_VALUES = ["H", "T"]

#input: none
#return: either "H" or "T"
#side effect: none
#description: simulates flipping a coin
def coinFlip():
    return random.choice(COIN_VALUES)

#input: none
#simulates how many times it takes to get "H" 5 x in a row
def simulateNumInARow():
    numInARow = 0
    total = 0
    while numInARow != 5:
        if coinFlip() == "H":
            numInARow += 1
        else:
            numInARow = 0
        total += 1
    return(total)

def main():
    #result = simulateNumInARow()
    #print("It took", result, "times to get heads 5 times in a row")
    result = 0
    for i in range(10):
        result += simulateNumInARow()
    print("It took", result/10, "times to get heads 10 times in a row")



main()
# Jean Tu
# ITP 115, Spring 2017
# Lab L7
# jeantu@usc.edu

import random

# 0 for rock, 1 for paper, or 2 for scissors.

# Input: none
# Output: none
# Print the rules of the game
def displayMenu():
    print()
    print("""Welcome! Let's play rock, paper, scissors.
The rules of the game are:
    Rock smashes scissors
    Scissors cut paper
    Paper covers rock
If both the choices are the same, it's a tie""")

# Input: none
# Output: return an integer
# Randomly choose a number representing the computer's choice
def getComputerChoice():
    computerChoice = random.randrange(3)
    return computerChoice

# Input: none
# Output: return the integer the user selected
# Asks the user for their choice: 0 for rock, 1 for paper, or 2 for scissors.
def getPlayerChoice():
    playerChoice = int(input("Please choose (0) for rock, (1) for paper or (2) for scissors: "))
    while(playerChoice > 2) or (playerChoice < 0):
        print("ERROR: you entered an invalid answer, try again!")
        playerChoice = int(input("Please choose (0) for rock, (1) for paper or (2) for scissors: "))
    return playerChoice

# Input: 2 integers (the choices)
# Output: return -1 if the computer won the round, return 1 if the player won the round, return 0 if there was a tie
# does the calculation of who won the game, 0 for rock, 1 for paper, or 2 for scissors.
def playRound(computerChoice, playerChoice):
    if computerChoice == playerChoice:  # if they tied
        print("You both choose the same. It's a tie!")
        return 0
    elif (computerChoice == 0 and playerChoice ==1): #c = rock, p = paper
        print("Paper beats rock. You win!")
        return 1
    elif (computerChoice ==1 and playerChoice == 2): #c = paper, p = scissors
        print("Scissors beats paper. You win!")
        return 1
    elif (computerChoice == 2 and playerChoice == 0): #C = scissors, p = rock
        print("Rock beats scissors. You win!")
        return 1
    elif(computerChoice == 1 and playerChoice ==0): #C = paper, p = rock
        print("Paper beats rock. The Computer wins!")
        return -1
    elif(computerChoice == 2 and playerChoice == 1): #c = scissors, p = paper
        print("Scissors beasts paper. The computer wins!")
        return -1
    elif(computerChoice == 0 and playerChoice == 2):  #c = rock, p = scissors
        print("Rock beats scissors. The Computer wins!")
        return -1
    else: #will never execute, but will have it here anyways
        return -1

#This prints the selection that was made before the playRound gets executed
def printChoice(person, playerChoice):
    if playerChoice == 0:
        print(person, "choose rock")
    elif playerChoice == 1:
        print(person, "choose paper")
    else:
        print(person, "choose scissors")


# Input: none
# Output: boolean
# Asks the user if they would like to play another round
def continueGame():
    print("Do you want to continue playing? Enter (y) for yes or (n) for no. ")
    contGame = input()
    if contGame.lower() == "y":
        return True
    else: #just setting the default to false if they enter in something in correct
        return False

def main():
    play = True
    computer = 0    # counter for the number of times that the computer wins
    user = 0        # counter for the number of times the user wins
    ties = 0        # counter for the number of times they have tied
    while play == True:
        displayMenu()
        computerChoice = getComputerChoice()
        playerChoice = getPlayerChoice()
        printChoice("You", playerChoice)
        printChoice("The computer", computerChoice)
        result = playRound(computerChoice, playerChoice)
        if result == 0: #there was a tie
            ties = ties + 1
        elif result == 1: #the player won
            user = user + 1
        else:
            computer = computer + 1
        play = continueGame()
    print()
    print("You won", str(user), "game(s).")
    print("The computer won", str(computer), "game(s).")
    print("You tied with the computer", str(ties), "game(s).")
    print()
    print("Thanks for playing!")


main()
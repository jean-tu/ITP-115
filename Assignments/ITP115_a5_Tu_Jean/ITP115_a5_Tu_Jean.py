# Jean Tu
# ITP 115, Spring 2017
# Assignment 5 - Tic Tac Toe
# jeantu@usc.edu
"""
The TicTacToe game for assignment 5 with some of the extra credit done,
I had done 2 out of the 3 parts
"""

import TicTacToeHelper
import random

# Input: List that represents the board, an integer corresponding to the index position
#        that the user would like to place their letter on
# Return: boolean value
# This will look @ the spot to return T if the spot is open, F if it's not in range/taken
def isValidMove(board_list, spot):
    if (board_list[spot] == "X ") or (board_list[spot] == "O "):
        return False
    # else it will return True
    return True

# Input: List, the index, what the user's letter is
# Return: None
# Takes the current board list and places the letter in the specified spot on the board
def updateBoard(board_list, spot, player_letter):
    board_list[spot] = player_letter + " "

#input: board
#user has a friend to play with
def playerMode(board, counter):
    noWinner = True
    player = "X"
    while (noWinner == True):
        TicTacToeHelper.printPrettyBoard(board)
        # TicTacToeHelper.printUglyBoard(board)  # using helper file to print the board
        invalid = True
        while invalid == True:
            if player == "X":
                position = int(input("Player X, pick a spot (0-8): "))
            else:
                position = int(input("Player O, pick a spot (0-8): "))
            if (position >= 0 and position <= 8):  # if they entered a valid spot
                invalid = False
            else:
                print("Invalid move, please try again.")
        if (isValidMove(board, position) == True):  # if the spot is available
            updateBoard(board, position, player)
        # end of invalid loop that continues to prompt the user until they enter something valid
        if player == "X":
            player = "O"
        else:
            player = "X"
        check = TicTacToeHelper.checkForWinner(board, counter)
        if check == "X ":  # x won
            TicTacToeHelper.printPrettyBoard(board)  # using helper file to print the board
            print("\nGame Over! \nPlayer X won!")
            noWinner = False
        elif check == "O ":  # o won
            TicTacToeHelper.printPrettyBoard(board)  # using helper file to print the board
            print("\nGame Over! \nPlayer O won!")
            noWinner = False
        elif check == "s":  # there was a stalemate
            TicTacToeHelper.printPrettyBoard(board)  # using helper file to print the board
            print("\nGame Over! \nStalemate reached!")
            noWinner = False
        # else: # the n case, where the game continues and noWinner remains False
        # change the player
        counter += 1  # another move has been made

def checker(board, counter):
    noWinner = True
    check = TicTacToeHelper.checkForWinner(board, counter)
    if check == "X ":  # x won
        TicTacToeHelper.printPrettyBoard(board)  # using helper file to print the board
        print("\nGame Over! \nPlayer X won!")
        noWinner = False
    elif check == "O ":  # o won
        TicTacToeHelper.printPrettyBoard(board)  # using helper file to print the board
        print("\nGame Over! \nPlayer O won!")
        noWinner = False
    elif check == "s":  # there was a stalemate
        TicTacToeHelper.printPrettyBoard(board)  # using helper file to print the board
        print("\nGame Over! \nStalemate reached!")
        noWinner = False
    else:
        noWinner = True
    return noWinner


# user has decided to play against the computer
def computerMode(board, counter):
    noWinner = True
    boardCopy = [0,1,2,3,4,5,6,7,8]
    while (noWinner == True):
        TicTacToeHelper.printPrettyBoard(board)
        # TicTacToeHelper.printUglyBoard(board)  # using helper file to print the board
        invalid = True
        while invalid == True:
            position = int(input("Player X, pick a spot (0-8): "))
            if (position >= 0 and position <= 8):  # if they entered a valid spot
                invalid = False
            else:
                print("Invalid move, please try again.")
        if (isValidMove(board, position) == True):  # if the spot is available
            boardCopy.remove(position)
            updateBoard(board, position,"X")
        # end of invalid loop that continues to prompt the user until they enter something valid
        if checker(board, counter) == False:
            noWinner = False #someone won
        computerChoice = random.choice(boardCopy)
        if (isValidMove(board, int(computerChoice)) == True):  # if the spot is available
            updateBoard(board, int(computerChoice), "O") #put the computer's mark there
            print("The Computer chose to put their letter @ " + str(computerChoice))
        counter += 1  # another move has been made
        noWinner = checker(board, counter)
# Input: none
# Return: none
# initialize the list representing the board
def playGame():
    counter = 1 # to keep track of how many moves have been made
    board = ["0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 "]
    computer = input("Would you like to play against the computer? (y/n): ")
    if computer.lower() == "y":
        computerMode(board, counter)
    else:
        playerMode(board, counter)



# Input: none
# Output: none
# Use a while loop to allow the user to keep playing a new game of tictac toe until they dont' want to play anymore
def main():
    print("Welcome to Tic Tac Toe!")
    play = True
    while(play == True):
        playGame()
        cont = input("Would you like to play another round? (y/n): ")
        print()
        if cont.lower() == "n": #if the user no longer wants to play
            print("Goodbye! Thanks for playing!")
            play = False


main() #calling ont the main function



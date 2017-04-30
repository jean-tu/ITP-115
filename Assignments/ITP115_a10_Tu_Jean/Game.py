from Vampire import Vampire
from Human import Human

# use a for loop using range to access each Human object in the list and display a number
def printHumans(humanList):
    index = 0
    print()
    for human in humanList:
        print(str(index) + ":  " + human.__str__())
        index += 1 #incrementing for the next user


#ask the user to enter an index number of a human
# include error checking to see if the number is within the range
# Human can't have < 0 quarts & vamp can't have more than 5
def performFeeding(humanList, vamp):
    print()
    numHumans = len(humanList)
    printHumans(humanList) # so that they can see who they have to choose from
    validChoice = False
    while validChoice == False:
        numChosen = input("Select a human: ")
        if numChosen.isdigit():
            numChosen = int(numChosen) #converting it into a number
            if numChosen < numHumans and numChosen >= 0: #seeing if it is a number within the range
                humanChosen = humanList[numChosen] #getting the human object
                if humanChosen.isAlive():
                    if not vamp.isStuffed():
                        print() # to make it look cleaner
                        vamp.suckBlood(humanChosen)
                        print() # just to make it look cleaner
                    #else the vamp is stuffed and can't drink anymore
                print(vamp.__str__())
                print(humanChosen.__str__())
                validChoice = True #to kick out of the loop


    #use the isAlive & isStuffed to check
    #call suckBlood & print out a message that indicates if vampire is stuffed or human is dead




def main():
    human1 = Human("Mary", 4, "A") #create the human objects (can be hardcoded)
    human2 = Human("Oscar", 3, "B")
    human3 = Human("Skye", 2, "O")
    humanList = [human1,human2, human3] #adding the hard coded humans into a list to be used later on

    nameBad = True
    while nameBad:
        vampName = input("What is the name of the Vampire? ")
        if vampName != " ":
            nameBad = False
    animalBad = True
    while animalBad:
        vampAnimal = input("What is the animal of the Vampire? ")
        if vampAnimal != " ":
            animalBad = False
    vamp = Vampire(vampName, 0, vampAnimal)#vampire object - ask the user for the name & animal & initially starving

    cont = True
    print("Welcome to Vampire vs. Human\n")
    while cont:
        choiceValid = False
        while choiceValid == False:
            # print()
            print("1) Print humans")
            print("2) Suck blood")
            choice = input("3) Exit ")
            if choice.isdigit():
                choice = int(choice) #converting it into a number2
                if choice == 1 or choice == 2 or choice == 3: #if it is a valid choice
                    if choice == 1:
                        printHumans(humanList)
                    elif choice == 2:
                        performFeeding(humanList, vamp)
                    else: # the user wants to stop playing
                        print("Thanks for playing")
                        print(vampName + " transforms into " + vampAnimal)
                        cont = False
                        choiceValid = True
                else:
                    print("Please choose a valid number")
                    print()
            else:
                print("Please enter a number")
                print()


    #Will use printHumans and performFeeding

main()
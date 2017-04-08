# Jean Tu
# ITP 115, Spring 2017
# Assignment 8: Object-Oriented Programming
# 4/2/2017
# Description:
#   We are creating an animal daycare

class Animal(object):
    def __init__(self, hunger, happiness, health, energy, age, name, species):
        self.__hunger = hunger
        self.__happiness = happiness
        self.__health = health
        self.__energy = energy
        self.__age = age
        self.__name = name
        self.__species = species

    def getHunger(self):
        return self.__hunger

    def getHappiness(self):
        return self.__happiness

    def getHealth(self):
        return self.__health

    def getEnergy(self):
        return self.__energy

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def getSpecies(self ):
        return self.__species

    def setHunger(self, newHunger):
        if newHunger > 100:
            newHunger = 100
        elif newHunger < 0:
            newHunger = 0
        self.__hunger = newHunger

    def setHappiness(self, newHappiness):
        if newHappiness > 100:
            newHappiness = 100
        elif newHappiness < 0:
            newHappiness = 0
        self.__self = newHappiness

    def setHealth(self, newHealth):
        if newHealth > 100:
            newHealth = 100
        elif newHealth < 0:
            newHealth = 0
        self.__health = newHealth

    def setEnergy(self, newEnergy):
        if newEnergy > 100:
            newEnergy = 100
        elif newEnergy < 0:
            newEnergy = 0
        self.__energy = newEnergy

    def setAge(self, newAge):
        if newAge > 100:
            newAge = 100
        elif newAge < 0:
            newAge = 0
        self.__age = newAge

    #create a string containing a well formatted message with all of the information about hte animal
    def __str__(self):
        print("Name:", self.getName(), "the", self.getSpecies().rstrip('\n'))
        print("Health:", self.getHealth())
        print("Happiness:", self.getHappiness())
        print("Hunger:", self.getHunger())
        print("Energy:", self.getEnergy())
        print("Age:", self.getAge())
        print("************************************")

    # • Input: none
    # • Return value: none
    # • Increase the animal’s happiness by 10 and
    # increase the animal’s hunger by 5.
    def play(self):
        self.setAge(int(self.getAge())+5) #increasing the hunger by 5
        self.setHappiness(int(self.getHappiness()) + 10) #increasing happiness by 10

    # Input: none
    # Return value: none
    # Decrease the animal’s hunger by 10.
    def feed(self):
        self.setHunger(int(self.getHunger())-10)

    # • Input: none
    # • Return value: none
    # • Decrease the animal’s happiness by 20 and increase the animal’s health by 20.
    def giveMedicine(self):
        self.setHappiness(int(self.getHappiness())-20)
        self.setHealth(int(self.getHealth())+20)

    # input: none
    # Return: none
    # Increase the animals energy by 20 and increase the animal's age by 1
    def sleep(self):
        self.setEnergy(int(self.getEnergy())+20)
        self.setAge(int(self.getAge())+1)

    def printStats(self):
        print("Name:", self.getName(), "the", self.getSpecies().rstrip('\n'))
        print("Health:", self.getHealth())
        print("Happiness:", self.getHappiness())
        print("Hunger:", self.getHunger())
        print("Energy:", self.getEnergy())
        print("Age:", self.getAge())
        print("************************************")

#input = string representing the name of the csv file
#return = list of Animal instance variables
#open the csv file and use each lien of data to create a new animal object
def loadAnimals(fileName):
    fileIn = open(fileName, "r")  # making the file readable
    animalList = []
    for line in fileIn:
        splitList = line.split(",")
        animal = Animal(splitList[0], splitList[1], splitList[2], splitList[3], splitList[4], splitList[5], splitList[6])
        animalList.append(animal)
    return animalList

#input = none
#return = none
# prints out the menu with all of the possible options to the user
def displayMenu():
    print("1) Play")
    print("2) Feed")
    print("3) Give Medicine")
    print("4) Sleep")
    print("5) Print an Animal's stats")
    print("6) View All Animals")
    print("7) Exit")


#input = list of animals
# return: the selected animal from the list
# print out menu w/ each animal's name & species
#ask the user to make a selection from the list -- HANDLE invalid inputs
# return the animal that corresponds with the selection
def selectAnimal(animalList):
    counter = 1
    print()
    for animal in animalList:
        print(str(counter)+")", animal.getName(), "the", animal.getSpecies().rstrip('\n'))
        counter += 1
    valid = False
    while valid == False:
        selected = input("\nPlease select an animal from the list (enter the 1-5): ")
        if selected.isdigit():
            selected = int(selected)
            if selected <= 5 and selected >= 1:
                return selected
            else:
                print("INVALID INPUT, please try again!!")
        else:
            print("INVALID INPUT, please try again!!")




#create a list of Animals from the loadAnimals function
#use a while loop to display the menu & ask the user to make a valid selection
def main():
    #Call on the loadAnimals function to create the list of animals
    fileName = "animals.csv"
    animalList = loadAnimals(fileName)
    print("Welcome to the Animal Daycare! Here is what we can do: ")
    cont = True
    while cont:
        print()
        displayMenu()
        choice = input("\nPlease make a selection: ")
        if choice.isdigit():
            choice = int(choice)
            if choice <= 7 and choice >= 1:
                if choice == 1: #play
                    selected = selectAnimal(animalList)
                    print("You played with " + animalList[selected-1].getName(),"the", animalList[selected-1].getSpecies().rstrip('\n') + "!")
                elif choice == 2: #feed
                    selected = selectAnimal(animalList)
                    animalList[selected - 1].feed()
                    print("You fed", animalList[selected-1].getName(),"the", animalList[selected-1].getSpecies().rstrip('\n') + "!")
                elif choice == 3: #Give medicine
                    selected = selectAnimal(animalList)
                    animalList[selected - 1].giveMedicine()
                    print("You gave", animalList[selected - 1].getName(), "the",
                          animalList[selected - 1].getSpecies().rstrip('\n') + " some medicine!")
                elif choice == 4: #sleep
                    selected = selectAnimal(animalList)
                    animalList[selected - 1].sleep()
                    print(animalList[selected - 1].getName(), "the",
                          animalList[selected - 1].getSpecies().rstrip('\n') + " took a nap!")
                elif choice == 5: #print animal stats
                    selected = selectAnimal(animalList)
                    animalList[selected - 1].printStats()
                elif choice == 6: #view all animals
                    for animal in animalList:
                        animal.printStats()
                elif choice == 7:
                    print("Thanks for visiting!! Goodbye!!")
                    cont = False #the user no longer wants to play
            else:
                print("*INVALID selection, please try again.")
        else:
            print("*INVALID selection, please try again.")


main()
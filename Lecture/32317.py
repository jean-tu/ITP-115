#Software Objects Part II
#Continuing offo f class on Tuesday

'''
Person

str name
float height
int age
str hairColor
str eyeColor
-----------
walk()
think()
eat()
sleep()
'''

'''

    species
    name
    breed
    color
    hasFur
    temperment

    l = [] #this is just a short cut that was created
    l2 = list() #this is the right way to declare a list

    class Pet(object):
        pass #allows you to come back to it alter to implement
'''

"""
Methods
    walk
    sleep
    eat
    cuddle
    speak
    findHumanAge
"""
import random

TEMPERAMENT = ["jolly", "distant", "lazy"]

class Pet(object):
    #Constructor - it constructs the objects
    def __init__(self, name, color, fur, age, species): #first parameter must always be self
        #take the input parameter and store them in the object (self)
        self.name = name
        self.color = color
        self.hasFur = fur
        self.age = age
        self.species = species
        self.temperament = random.choice(TEMPERAMENT)
        print(self.name, "is adorable and the color", self.color, "and has ", self.hasFur, "fur")

    def cuddle(self):
        if self.temperament == "distant":
            print(self.name, "does not want to cuddle right now. Please try again later.")
        else:
            print(self.name, "would love some scratches")

    def findHumanAge(self):
        humanAge = 0
        if self.species == "dog":
            humanAge =  7*self.age
        elif self.species == "tortoise":
            humanAge =  self.age*.8
        else:
            humanAge = self.age
        return humanAge

    def needsCoat(self, outsideTemp):
        if outsideTemp  < 55:
            return True
        elif outsideTemp >=  55 and outsideTemp < 70 and self.hasFur == False:
            return True
        else:
            return False


    #str never takes input
    #str ALWAYS returns a string
    #str NEVER prints anything
    def __str__(self): #this is what will return if you try to print the object
        msg = self.name + " is a " + str(self.age) + " year old " + self.species
        return msg

def main():
    bruno = Pet("Bruno", "brown", True, 12, "dog") # creates a unique PET object from the general PET class
    bart = Pet("Bart", "green", False, 30, "tortoise")
    print()
    bruno.cuddle()
    bart.cuddle()
    print()
    print("bruno is", bruno.findHumanAge(), "in human years")
    print("bart is", bart.findHumanAge(), "in human years")
    print()
    print(bruno)
    print(bart)
    print()

    if bruno.needsCoat(15) == True:
        print("Brrr! Get your pet a caot")
    else:
        print("no worries, your pet is fine")

main()
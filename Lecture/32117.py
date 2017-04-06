#Software Objects

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

class Pet(object):
    #Constructor
    def __init__(self, name, color, fur): #first parameter must always be self
        #take the input paremeter and store them in the object (self)
        self.name = name
        self.color = color
        self.hasFur = fur
        print(self.name, "is adorable and the color", self.color, "and has ", self.hasFur, "fur")


def main():
    bruno = Pet("Bruno", "brown", True) # creates a unique PET object from the general PET class
    bart = Pet("Bart", "green", False)


main()
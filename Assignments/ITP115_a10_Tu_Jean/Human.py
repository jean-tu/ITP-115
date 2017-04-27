from Being import Being

class Human(Being):
    def __init__(self, name, quarts, bloodType):
        super().__init(self, name, quarts) #calling on the superclass init
        self.__bloodType = bloodType

    def getBloodType(self):
        return self.__bloodType

    def setBloodType(self, newType):
        self.__bloodType = newType

    def isAlive(self):
        if (self.__quarts > 0):
            return True
        else:
            return False

    def __str__(self):
        msg = "Human " + self.__name + " has " + str(self.__quarts) + " of type " \
            + self.__bloodType + " blood."
        return msg

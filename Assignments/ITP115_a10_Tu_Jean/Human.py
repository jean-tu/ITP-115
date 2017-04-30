from Being import Being

class Human(Being):
    def __init__(self, name, quarts, bloodType):
        super().__init__(name, quarts) #calling on the superclass init
        self._bloodType = bloodType

    def getBloodType(self):
        return self._bloodType

    def setBloodType(self, newType):
        self._bloodType = newType

    def isAlive(self):
        if (self._quarts > 0):
            return True
        else:
            return False

    def __str__(self):
        msg = "Human " + self._name + " has " + str(self._quarts) + " of type " \
            + self._bloodType + " blood."
        return msg

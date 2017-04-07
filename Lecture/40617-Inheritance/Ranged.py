# defining the range weapon class that inherits from Weapon
from Weapon import Weapon

"""
New Attributes
    * Range/distance
    * num Amo (capacity)
    * accuracy
"""

class Ranged(Weapon):# don't use object, put the class you are inheriting from
    def __init__(self, attack, name, capacity ):
        #speed is an attribute unique to Melee class NOT from Weapon class
        super().__init__(attack, name)
        self.__capacity = capacity #int

    def getCapacity(self):
        return self.__capacity

    def reduceCapacity(self, num):
        if self.__capacity - num >= 0:
            self.__capacity -= num
            return True
        else:
            return False #don't do anything b/c you don't want it to go negative

    #Override a method from the parent class
    def __str__(self):
        #use the parent class version of String method
        msg = super().__str__() + ", Capacity: " + str(self.__capacity)
        return msg

    #override the use method
    def use(self):
        result = self.reduceCapacity(1) # result is a boolean
        if result == True:
            # we were able ot use the ranged weapon
            print("Firing " + self.getName() + " (capacity: " + str(self.getCapacity()) + ")")


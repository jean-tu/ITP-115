# defining the melee weapon class that inherits from Weapon
from Weapon import Weapon

class Melee(Weapon):# don't use object, put the class you are inheriting from
    def __init__(self, attack, name, speed):
        #speed is an attribute unique to Melee class NOT from Weapon class
        super().__init__(attack, name)
        self.__speed = speed #int

    #Override a method from the parent class
    def __str__(self):
        #use the parent class version of String method
        msg = super().__str__() + ", SpeedL : " + str(self.__speed)
        return msg

    #override the use method
    def use(self):
        print("using " + self.getName()) #becuase it's a child of the Weapon class, it will also have the method that the Weapon class has

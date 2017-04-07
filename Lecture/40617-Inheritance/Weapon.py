
class Weapon(object):
    """
        all weapons:
        * Attack value/damage
        * name
    """

    def __init__(self, attack, name):
        self.__attackValue = attack
        self.__name = name

    def getAttackValue(self):
        return self.__attackValue

    def getName(self):
        return self.__name

    def __str__(self):
        msg = self.__name + ", Attack: " + str(self.getAttackValue())
        return msg

    def use(self): # method that we want all of the children to override
        print("Using " + self.__name)

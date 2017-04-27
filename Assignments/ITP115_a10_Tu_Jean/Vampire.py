from Being import Being

class Vampire(Being):
    MAX_BLOOD = 5
    HUNGER_LEVELS = ["starving", "hangry", "hungry", "content", "full", "stuffed"]

    def __init__(self, name, quarts, animal):
        super().__init(name, quarts)
        self.__animalForm = animal

    def getAnimalForm(self):
        return self.__animalForm

    def setAnimalForm(self, newForm):
        self.__animalForm = newForm

    def getHunger(self): #returns a string that will tell how hungry they are
        level = Vampire.HUNGER_LEVELS[self.__quarts] #the string
        msg = self.__name + " is " + level
        return msg

    def isStuffed(self):
        if self.__quarts == Vampire.MAX_BLOOD:
            return True
        else:
            return False

    def suckBlood(self, Human):
        Human.decreaseQuarts() #suck the human blood
        self.increaseQuarts()   #increase the vampire blood

    def __str__(self):
        levelOfHunger = Vampire.HUNGER_LEVELS[self.__quarts]
        msg = self.__name + " is " + levelOfHunger
        return msg 


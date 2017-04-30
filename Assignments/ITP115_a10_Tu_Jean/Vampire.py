from Being import Being

class Vampire(Being):
    def __init__(self, name, quarts, animal):
        super().__init__(name, quarts)
        self.__animalForm = animal

    MAX_BLOOD = 5
    HUNGER_LEVELS = ["starving", "hangry", "hungry", "content", "full", "stuffed"]

    def getAnimalForm(self):
        return self._animalForm

    def setAnimalForm(self, newForm):
        self._animalForm = newForm

    def getHunger(self): #returns a string that will tell how hungry they are
        level = Vampire.HUNGER_LEVELS[self._quarts] #the string
        msg = self._name + " is " + level
        return msg

    def isStuffed(self):
        if self._quarts == Vampire.MAX_BLOOD:
            return True
        else:
            return False

    def suckBlood(self, Human):
        Human.decreaseQuarts() #suck the human blood
        self.increaseQuarts()   #increase the vampire blood

    def __str__(self):
        levelOfHunger = Vampire.HUNGER_LEVELS[self._quarts]
        msg = self._name + " is " + levelOfHunger
        return msg 


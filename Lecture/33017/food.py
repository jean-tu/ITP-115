"""
Attributes of a Fruit
* color
* vegetarian
* spiciness


Spicyness scale
0 = not spicy
1 = spicy
2 = super spicy
3 = DANGER!
"""
class Food(object):
    SPICINESS_LEVELS = ["not spicy", "spicy", "super spicy", "DANGER!"]

    def __init__(self, c, v, s):
        self.__color = c
        self.__isVegetarian = v
        self.__spiciness = s

    # you should build getters/setters for all
    def getColor(self):
        return self.__color

    def isVegetarian(self):
        return self.isVegetarian()

    def getSpiciness(self):
        return Food.SPICINESS_LEVELS[self.__spiciness]



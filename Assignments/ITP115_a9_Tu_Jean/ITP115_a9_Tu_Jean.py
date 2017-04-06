# Jean Tu
# ITP 115, Spring 2017
# Assignment 9: OOP Part 2 (Superheros)
# 4/9/2017
# Description:
#   making a simulation of a fight with superheroes

class Superhero(object):
    def __init__(self, name, type, attack):
        self.__name = name
        self.__type = type
        self.__attack = attack
        self.__health = 100

    def getName(self):
        return self.__name

    def getAttack(self):
        return self.__attack

    def getHealth(self):
        return self.__health

    def getType(self):
        return self.__type

    def loseHealth(self, opponentAttack):
        self.__health = self.__health - opponentAttack

    def isDead(self):
        if self.__health <= 0:
            return True
        else:
            return False

    def __str__(self):
        message = self.__name + " the "+ self.__type+ " has "+str(self.__attack) \
            + " attack points and currently has "+ str(self.__health) + " points of health. "
        return message


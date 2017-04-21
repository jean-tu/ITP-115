# Superhero.py

import random

# Superhero class
# class/static attributes: MIN_HEALTH, MAX_HEALTH & MAX_ATTACK
# private instance attributes: name, health, attack
# methods: get/set name
# more methods: isDead, loseHealth, reset, getStats, __str__
# loseHealth

class Superhero(object):
    # class/static attributes
    MIN_HEALTH = 70  # minimum value for starting health
    MAX_HEALTH = 100  # maximum value for starting health
    MAX_ATTACK = 20

    # constructor method
    def __init__(self, name="Superhero"):
        self.name = name
        self.health = random.randrange(Superhero.MIN_HEALTH, Superhero.MAX_HEALTH + 1)
        self.attack = random.randrange(1, Superhero.MAX_ATTACK + 1)

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def isDead(self):
        if self.health <= 0:
            return True
        else:
            return False
			
    def isAlive(self):
        return not self.isDead()

    def loseHealth(self, points):
        if points > self.health:
            self.health = 0
        else:
            self.health -= points

    def reset(self):
        self.health = random.randrange(Superhero.MIN_HEALTH, Superhero.MAX_HEALTH + 1)
        self.attack = random.randrange(1, Superhero.MAX_ATTACK + 1)

    def getStats(self):
        msg = "\nHealth = " + str(self.health) + "\n"
        return msg

    def __str__(self):
        msg = self.name + "\nHealth = " + str(self.health)
        msg += "\nAttack = " + str(self.attack) + "\n"
        return msg

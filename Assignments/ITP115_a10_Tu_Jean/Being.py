# This is the parent class

class Being(object):
    def __init__(self, name, quarts):
        self._name = name
        self._quarts = quarts

    def getName(self):
        return self._name

    def getQuarts(self):
        return self._quarts

    def setName(self, name):
        self._name = name

    def setQuarts(self, quarts):
        self._quarts = quarts

    def increaseQuarts(self): #increase the quarts of blood by 1
        self._quarts += 1

    def decreaseQuarts(self): #decrease the quarts of blood by 1
        self._quarts -= 1

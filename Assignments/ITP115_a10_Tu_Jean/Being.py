# This is the parent class

def Being(object):
    def __init__(self, name, quarts):
        self.__name = name
        self.__quarts = quarts

    def getName(self):
        return self.__name

    def getQuarts(self):
        return self.__quarts

    def setName(self, name):
        self.__name = name

    def setQuarts(self, quarts):
        self.__quarts = quarts

    def increaseQuarts(self): #increase the quarts of blood by 1
        self.__quarts += 1

    def decreaseQuarts(self): #decrease the quarts of blood by 1
        self.__quarts -= 1

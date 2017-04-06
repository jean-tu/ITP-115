# Jean Tu
# ITP 115, Spring 2017
# Lab practical L14
# jeantu@usc.edu

class Coffee(object):
    STATUSES = ["ordered", "completed"]
    def __init__(self, size, desc, customer):
        self.__size = size              #size of drink s,m,l
        self.__desc = desc              # description of the drink
        self.__customer = customer      # name of the customer
        self.__status = 0          # 0 - drink not made, 1 - drink completed, will start off w/ 0

    def setCompleted(self):
        self.__status = 1

    def getSize(self):
        return self.__size

    def getDescription(self):
        return self.__desc

    def getCustomer(self):
        return self.__customer

    def getStatus(self):
        return self.__status

    def __str__(self):
        #return a string containing information about coffee object
        #use the class variable
        return(self.__size + " " + self.__desc + " for n" + self.__customer +  " (" + Coffee.STATUSES[self.__status]+ ")")





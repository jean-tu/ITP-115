# Jean Tu
# ITP 115, Spring 2017
# Lab practical L14
# jeantu@usc.edu

from Coffee import Coffee

class Barista(object):
    MAXORDERS = 5

    def __init__(self, name):
        self.__name = name
        self.__orders = [] #list of coffee objects | starts off empty

    # Tkae coffee order by asking the user's name
    def takeOrder(self):
        print("\nHello, my name is", self.__name, "and I am your barista.")
        desc = input("What drink do you want?: ")
        size = input("What size drink would you like: ")
        name = input("What is your name?: ")
        #create the coffee object
        newOrder = Coffee(size, desc, name)
        self.__orders.append(newOrder) #adding the new order to the list
        print(newOrder.getSize(), newOrder.getDescription(), "for", newOrder.getCustomer(), "("+ Coffee.STATUSES[newOrder.getStatus()] + ")")

    #returns a boolean
    def isAcceptingOrders(self):
        if len(self.__orders) < Barista.MAXORDERS:
            return True
        else:
            return False

    def makeDrinks(self):
        print("\nHere are the completed orders: ")
        for order in self.__orders:
            order.setCompleted() #using the coffee class's setCompleted to change it
            # print(order.getSize, order.getDescription, "for", order.getCustomer(), "("+ Coffee.STATUSES[order.getStatus()]+")")
            print("\t", order.__str__()) #to print out the function
        self.__orders = []  #reset the barista's order to an empty list

    def __str__(self):
        return ("Hello, my name is", self.__name, "and I am your barista.")
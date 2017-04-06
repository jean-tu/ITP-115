
class Shape(object):
    def __init__(self, n):
        self.__name = n

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def __str__(self):
        msg = "Name: " + self.__name
        return msg

    #guarantees that all children will have this method that they will need to redefine
    def calcArea(self): #will be overridden later
        return 0

#==========================

class Rectangle(Shape):
    def __init__(self, name, length, width): #needs name b/c it's what the parent took
        #call the the parent constructor
        super().__init__(name)
        self.__length = length
        self.__width = width

    #Define getters and setters of and width
    def getLength(self):
        return self.__length

    def setLength(self, length):
        self.__length = length

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    #Overriding the parent method
    def calcArea(self):
        return self.__length * self.__width

    def __str__(self):
        #call the parent version of this method
        output = super().__str__()
        output += ", length: " + str(self.__length) + ", width: " + str(self.__width)
        return output

    def summary(self):
        print("The rectangle", self.getName(), "is", self.calcArea(), "square inches")

def main():
    r1 = Rectangle("phone", 4, 2)
    r2 = Rectangle("table", 48, 36)

    print("The length of", r1.getName(), "is", r1.getLength())
    print(r1)
    print("The area of", r1.getName(), "is", r1.calcArea(), "square inches")
    print("The length of", r2.getName(), "is", r2.getLength())
    print(r2.__str__())
    r1.summary()

main()
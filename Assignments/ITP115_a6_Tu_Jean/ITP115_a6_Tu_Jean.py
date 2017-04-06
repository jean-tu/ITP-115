# Jean Tu
# ITP 115, Spring 2017
# Assignment 6 - EPA File Processing
# jeantu@usc.edu

"""
This Files assignment takes in select information from the imported csv file that the user selects.
We run through the desired database to find out which cars get the best highway mpg and which ones get the worst.
"""

#GLOBAL VARIABLES
# creating empty lists "table"
carType = []
manufacturer = []
carLine = []
highwayMPG = []
year = 0

#input the file that will be set
#output none
# will set the year that the user wants to look at
def yearRequest():
    global year
    yearInRange = False
    while yearInRange == False:
        year = int(input("What year would you like to view data for? (2008 or 2009): "))
        if year == 2008:
            fileIn = "epaVehicleData2008.csv"
            yearInRange = True
        elif year == 2009:
            fileIn = "epaVehicleData2009.csv"
            yearInRange = True
        else: #out of range & loop again
            print("* Invalid input please try again ")
    return fileIn

def resultRequest():
    fileOut = input("Enter the filename to save results to: ")
    #print(fileOut[len(fileOut)-4:len(fileOut)])
    return fileOut

def parse(fileIn):
    global carType
    global manufacturer
    global carLine
    global highwayMPG
    count = 0 #to skip the first line with the headers from being added to the lists
    for line in fileIn:
        splitList = line.split(",")
        if splitList[0] == "CLASS":
            count += 1
        # print("1", splitList)
        elif "PICKUP" not in splitList[0] and "VAN" not in splitList[0]: #if the car is not a VAN/PICKUP
            carType.append(splitList[0])
            manufacturer.append(splitList[1])
            carLine.append(splitList[2])
            highwayMPG.append(splitList[9])


# Function doesn't return anything
def findMax(fileOut):
    global carType
    global manufacturer
    global carLine
    global highwayMPG
    maxMPG = 0
    for hMPG in highwayMPG:
        hMPG = int(hMPG)
        if hMPG > maxMPG: #it's greater so we want to save it
            maxMPG = hMPG
        #else, move on to the next
    print("Maximum Mileage (highway): " + str(maxMPG), file=fileOut)
    index = 0
    for hMPG in highwayMPG:
        hMPG = int(hMPG)
        if hMPG == maxMPG: #write the car's information to the document
            print("     " + manufacturer[index] + " " + carLine[index], file=fileOut)
        index += 1
    print("", file=fileOut)

# input: the file, to be able to
# output/return: none
def findMin(fileOut):
    global carType
    global manufacturer
    global carLine
    global highwayMPG
    minMPG = 1000  #setting it to a high number
    for hMPG in highwayMPG:
        hMPG = int(hMPG)
        if hMPG < minMPG:  # it's greater so we want to save it
            minMPG = hMPG
            # else, move on to the next
    print("Minimum Mileage (highway):" + str(minMPG), file=fileOut)
    index = 0 #to keep track of what index to grab the car's info
    for hMPG in highwayMPG:
        hMPG = int(hMPG)
        if hMPG == minMPG:  # write the car's information to the document
            print("     " + manufacturer[index] + " " + carLine[index], file=fileOut)
        index += 1



def printHeader(year, fileOut):
    print("EPA Highway MPG Calculator (" + str(year) + ") \n", file=fileOut)
    print("---------------------------------\n", file=fileOut)

def main():
    global carType
    global manufacturer
    global carLine
    global highwayMPG
    global year
    print("Welcome to EPA Mileage Calculator")
    fileInName = yearRequest()
    fileIn = open(fileInName, "r") #only allowing it to read
    #print(fileIn.title())  #testing
    fileOutName = resultRequest()
    fileOut = open(fileOutName, "w") #allowing it to write to the file
    parse(fileIn)
    printHeader(year, fileOut)
    findMax(fileOut)
    findMin(fileOut)
    print("Operation Success!")
    #remember to close the files
    fileIn.close()
    fileOut.close()
main()
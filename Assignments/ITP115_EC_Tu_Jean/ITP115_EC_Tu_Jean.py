# Jean Tu
# ITP 115, Spring 2017
# Extra Credit: Web Scraping
# jeantu@usc.edu

#This is an extra credit assignment where we would do web scraping to help a user
# figure out the classes that are being offered for a certain amount of units that they'd like tos search for

from bs4 import BeautifulSoup
import urllib.request # in order to be able to request the URL

#will return the number of units that the user would like to search for
def searchForClasses():
    #ask user for number of units they want to search for
    validEntry = False
    numUnits = 0
    while validEntry == False:
        numUnits = input("Enter the number of units you wish to search for classes by (1-4): ")
        if numUnits.isdigit(): #checking that the user input a digit, otherwise it's invalid input
            numUnits = int(numUnits)
            if numUnits >= 1 and numUnits <=4: #checking to see whether or not the input was a valid range
                print("See 'results.txt' for your results.")
                validEntry = True
            else:
                print("*Invalid input, please try again.")
        else:
            print("*Invalid input, please try again.")
    return numUnits

def main():
    #request the web page we want to parse from its url
    url = "http://classes.usc.edu/term-20171/classes/itp/"
    page = urllib.request.urlopen(url)

    #creating the file that is going to be written to
    fileOut = open("results.txt", "w")

    #make the soup
    soup = BeautifulSoup(page.read(), "html.parser")

    #ask the user the number units they would like to search for in an ITP class
    numUnits = searchForClasses()

    #writing the simple statement into the file
    print("Here are all of the ITP classes that are "+ str(numUnits) + " units:\n ", file=fileOut)

    #getting the courses
    for tag in  soup.find_all('div', attrs={'class': 'course-info expandable'}):
        # print("tag", tag)
        list = [] #to append to
        for title in tag.find('div', attrs={'class': 'course-id'}) :
            courseFound = False
            wholeTitle = title.text
            if str(numUnits) + ".0 units" in wholeTitle:
                print(title.text, file=fileOut)  # printing the name of the course to results.txt
                courseFound = True

            outsideTable = tag.find('div', attrs={'class': 'course-details'}) #finding where the table is
            table = outsideTable.find('table') #creating a table variable for a more refied search
            index = 0
            for time in table.find_all('td', attrs={'class':'time'}): #getting the time of the class
                if courseFound == True:
                    list.append("Time: " + time.text)
                    # print("Time: " + time.text, file=fileOut)
                    index += 1  # increment
            index = 0
            for registered in table.find_all('td', attrs={'class': 'registered'}): #getting the # of people registered
                if courseFound == True:
                    list[index] +=  ", Registered: " + registered.text
                    # print("Registered: " + registered.text, file=fileOut)
                    index += 1  # increment
            index = 0
            for instructor in table.find_all('td', attrs={'class': 'instructor'}): #getting the instructors
                if courseFound == True:
                    if instructor.text == "":
                        list[index] = list[index] + ", Instructor: -  "
                    else:
                        list[index] = list[index] + ", Instructor: " + instructor.text
                     # print("Instructor " + instructor.text, file=fileOut)
                    index += 1 # increment
            for item in list:
                print(item, file=fileOut) #writing the line to the file
            if courseFound == True:
                print("", file=fileOut) #to make a space
    fileOut.close() #closing the file

main()



# Jean Tu
# ITP 115, Spring 2017
# Lab L13
# jeantu@usc.edu

MAX_COURSES = 6

class Student(object):
    # Input: (2) name and ID, number
    # Return value: none
    def __init__(self, studentName, studentID):
        self.__name = studentName
        self.__studentID = studentID
        self.__courses = [] #making an empty list for all users

    # Input: none
    # Return value: the student's name
    def getName(self):
        return self.__name

    def setName(self, newName):
        if newName != "" and isinstance(newName, str):
            self.__newName
        else:
            print("Please enter a valid name")

    def getID(self):
        return self.__studentID

    def setID(self, newID):
        self.__studentID = newID

    def getCourses(self):
        return self.__courses

    # Input: none
    # Return Value: the number of courses the student is registered in
    def getNumberOfCourses(self):
        return len(self.__courses)

    # Input: the name of the course being added
    # Return value: boolean indicating the success of adding a new course
    # Depending on whether or not the student has registered for hte max # of courses
    #  , add the new course to the student's list fo coureses
    def addCourse(self, course):
        if self.getNumberOfCourses() < MAX_COURSES:
            self.__courses.append(course)
            return True
        else:
            return False

    def __str__(self):
        msf = "Student: " + self.__name + ", ID: " + self.__studentID + " enrolled in " \
                        + str(len(self.__courses)) + " courses"

def printStudents(studentList):
    print("")
    for student in studentList:
        print("Student", student.getName() + ", ID:", str(student.getID()), "enrolled in",
              str(student.getNumberOfCourses()), "courses:")
        studentCourses = student.getCourses() #returns a list
        for course in studentCourses: #iterate through the list of courses
            print("\t-", course)

def main():
    default1 = Student("Batman", "00")
    default2 = Student("Joker", "01")
    default3 = Student("Penguin", "13")
    default4 = Student("Batwoman", "88")

    studentList = [default1, default2, default3, default4]
    studentList[0].addCourse("ITP 115")
    studentList[1].addCourse("ITP 115")
    studentList[2].addCourse("ITP 115")
    studentList[3].addCourse("ITP 115")

    print("Welcome to the student registration system!")
    continueLoop = True
    while continueLoop:
        print("\nStudents: ")
        counter = 1
        for student in studentList:
            print(str(counter) + ") " + student.getName())
            counter += 1
        good = False
        while good == False:
            choice = input("Select a student form the list (1-4): ")
            if choice.isdigit():
                choice = int(choice)
                good = Truen

        #getting the student
        selectedStudent = studentList[choice-1] #b/c array indexing
        course = input("Enter the course the student is registering for: ")
        success = selectedStudent.addCourse(course)
        if success:
            print("Course registration successful.")
        else: #False was returned
            print("Course registration was unsuccessful.")
        cont = input("Would you like to continue registering? (y/n): ")
        if cont.lower() == "n":
            continueLoop = False
        #else is that they want to continue and will go back to the top of the while loop
    printStudents(studentList)

main()

from Story import Story


class MadLib(Story):
    def __init__(self):
        super().__init__()
        self.nounArr = ["I", "He", "She", "They", "Cat", "Dog", "Mountain"]
        self.verbArr = ["jumped", "slid", "smiled", "walk", "run", "laughed"]
        self.emotion = ["happy", "eager", "brave", "scared", "calm"]
        self.name = ["Alex", "John", "Alice", "Jane", "Bob", "Candice", "Tommy", "Helen"]
        self.place = ["Chicago", "Los Angles", "San Fransisco", "Florida", "Seattle"]

    # returns the list of stories for the user to select
    def getListOfStories(self): #will go though the master.txt file to get the file names of the files
        listofStories = [] #creating a blank list
        fileIn = open("Stories/master.txt", "r") #go into the folder to get the stories
        for line in fileIn:
            # print(line)
            listofStories.append(line)
        return listofStories

    def parser(self, story):
        print("called on the parser function")

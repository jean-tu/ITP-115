from Story import Story


class MadLib(Story):
    def __init__(self):
        super().__init__()
        self.nounArr = ["I", "He", "She", "They", "Cat", "Dog", "Mountain"]
        self.verbArr = ["jumped", "slid", "smiled", "walk", "run", "laughed"]
        self.emotion = ["happy", "eager", "brave", "scared", "calm"]
        self.name = ["Alex", "John", "Alice", "Jane", "Bob", "Candice", "Tommy", "Helen"]
        self.place = ["Chicago", "Los Angles", "San Fransisco", "Florida", "Seattle"]

    def getListOfStories(self, master): #will go though the master.txt file to get the file names of the files
        pass

    def parser(self):
        pass

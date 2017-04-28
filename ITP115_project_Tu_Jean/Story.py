from os import system

class Story(object):
    def __init__(self):
        self.story = "Default story"

    def __str__(self):
        return("Story Object")

    def read(self, story): #this will read the story that was passed in
        system("say " + story)

    def save(self, story): #allows the user to save the file
        pass
# st = Story()
# "text"
# st.read(st.story)
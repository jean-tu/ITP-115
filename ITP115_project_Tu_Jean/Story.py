from os import system

class Story(object):
    def __init__(self):
        self.story = "Default story"

    def __str__(self):
        return("Story Object")

    def read(self, story): #this will read the story that was passed in
        system("say " + story)

    def save(self, story, filename): #allows the user to save the file
        fileOut = open("Stories/Usermade/" + filename, "w") #will save the file into Stories
        print(story, file=fileOut) #writing the story to the file
        fileOut.close() #close the file

# st = Story()
# "text"
# st.read(st.story)
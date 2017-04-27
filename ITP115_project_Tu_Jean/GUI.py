from tkinter import *

class GUI(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        #First window information
        self.readMyStoryLabel = Label(self, text="readMyStory", background="azure", font=("Courier", 30))
        # self.readMyStoryLabel.grid(row=0, column=2)
        self.readMyStoryLabel.grid()
        self.infoText1 = Label(self, text="You have the option of creating your own story or \n "
                                          "filling in a MadLibs that will then be read out for you \n"
                                          "at the end! You will even get the option to \n"
                                          "save your wonderful story!",
                              background="azure", font=("Courier", 12))
        self.infoText1.grid()
        # self.infoText1.grid(row=1, column=2)
        # buttons
        self.createOwnButton = Button(self, text="Create Own!", command=self.createOwn)#.pack(side=LEFT)
        self.createOwnButton.grid()
        # self.createOwnButton.grid(row=2, column=2)
        self.madLibsButton = Button(self, text="MadLibs!", command=self.madLibs)#.pack(side=RIGHT)
        self.madLibsButton.grid()
        # self.madLibsButton.grid(row=2, column=2)

    def createOwn(self): #user decided to create their own story
        pass


    def madLibs(self): #user wanted to do the mad libs version
        pass
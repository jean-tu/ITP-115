from tkinter import *
import tkinter.messagebox

class GUI(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.__master = master
        #First window information
        self.readMyStoryLabel = Label(self, text="readMyStory", font=("Courier", 30))
        # self.readMyStoryLabel.grid(row=0, column=2)
        self.readMyStoryLabel.grid()
        self.infoText1 = Label(self, text="You have the option of creating your own story or \n "
                                          "filling in a MadLibs that will then be read out for you \n"
                                          "at the end! You will even get the option to \n"
                                          "save your wonderful story!",
                              font=("Courier", 12))
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
        tkinter.messagebox.showinfo("Create Own!", "You have chosen to create your own story!")
        self.infoText1.grid_remove() #this is to remove the information text
        self.madLibsButton.grid_remove()
        self.createOwnButton.grid_remove()

    def madLibs(self): #user wanted to do the mad libs version
        tkinter.messagebox.showinfo("MadLibs!", "You have chosen to do a MadLib Story!")
        #clear the main and start
        self.infoText1.grid_remove()  # this is to remove the information text
        self.madLibsButton.grid_remove()
        self.createOwnButton.grid_remove()

        self.selectStoryText= Label(self, text="Please select a story below")
        self.madLibsStoryList = Listbox(self.__master) #passing in the window to add it
        self.madLibsStoryList.insert(1, "Python")
        self.madLibsStoryList.insert(2, "Perl")
        self.madLibsStoryList.insert(3, "C")
        self.madLibsStoryList.insert(4, "PHP")
        self.madLibsStoryList.insert(5, "JSP")
        self.madLibsStoryList.grid()

        self.selectStoryButton = Button(self, text="Select", command=self.setSelected)
        self.selectStoryButton.grid()


    def setSelected(self):
        selected = self.madLibsStoryList.get(ACTIVE)
        return selected
from tkinter import *
from Superhero import Superhero

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(background="#ffcc00")
        self.grid()

        #superhero data
        self.p1 = Superhero("Player 1")
        self.p2 = Superhero("Player 2")


        #label
        self.playerLabel = Label(self, text="Enter player name", background="#ffcc00")
        self.playerLabel.grid(row=0, column=1);

        #player 1 entry
        self.p1Entry = Entry(self)
        self.p1Entry.grid(row=1, column=0)

        # player 2 entry
        self.p2Entry = Entry(self)
        self.p2Entry.grid(row=1, column=2)

        # button
        self.startButton = Button(self, text="Start Game", command=self.startGame)
        self.startButton.grid(row=2, column=1)

        # text boxes that display the information for p1
        self.p1Text = Text(self,width=20, height=25)
        self.p1Text.grid(row=3, column=0)

        # hero stats
        self.heroStatsLabel = Label(self, text="Hero Stats", background="#ffcc00")
        self.heroStatsLabel.grid(row=3, column=1)

        # text boxes that display the information for p2
        self.p2Text = Text(self, width=20, height=25)
        self.p2Text.grid(row=3, column=2)

        # button for fighting
        self.fightButton = Button(self, text="Fight!", command=self.fight)
        self.fightButton.grid(row=4, column=1)

    def startGame(self):
        #set the name of each of the superheroes
        self.p1.setName(self.p1Entry.get())
        # self.p1Entry.delete(0, END)

        self.p2.setName(self.p2Entry.get())
        # self.p2Entry.delete(0, END)

        #display the round information
        # message1 = self.p1.getName()+ " has health of " + self.p1.getStats()
        # //print(message1)
        # self.p1Text.insert(0.0, message1)
        # message2 = self.p2.getName() + " has health of " + self.p2.getStats()
        # self.p1Text.insert(0.0, message2)


        self.p1Text.insert(0.0, self.p2.__str__())
        self.p2Text.insert(0.0, self.p1.__str__())

    def fight(self):
        while(self.p1.isAlive() == True and self.p2.isAlive()) == True:
            self.p1.loseHealth(self.p2.attack)
            self.p2.loseHealth(self.p1.attack)

            self.p1Text.insert(END, self.p1.getStats())
            self.p2Text.insert(END, self.p2.getStats())
        if self.p1.isAlive == True and self.p2.isAlive() == False:
            self.p2Text.insert(END, "Dead")
            self.p1Text.insert(END, "Winner")

        elif self.p2.isAlive() == True and self.p1.isAlive() == False:
            self.p1Text.insert(END, "Dead")
            self.p2Text.insert(END, "Winner")
        else:
            self.p1Text.insert(END, "Fainted")
            self.p2Text.insert(END, "Fainted")




    def resetGame(self):
        pass
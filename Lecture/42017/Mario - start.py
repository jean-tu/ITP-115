# Mario.py - Game

import random
from tkinter import *

# Lay out our GUI
# parent is Frame
class Application(Frame):
    # class attributes
    WIDTH = 1000
    HEIGHT = 700
    IMAGE_SIZE = 60

    def __init__(self, window):
        # call parent contructor, Frame
        super().__init__(window)
        self.grid()  # displays
        self.goombaMovementCounter = 1

        # Canvas - private instance variable
        self.__canvas = Canvas(self, width=Application.WIDTH, height=Application.HEIGHT, bg="black")
        self.__canvas.grid()

        # Images - private instance variables
        self.imageMario = PhotoImage(file="mario.gif")
        self.imageGoomba = PhotoImage(file="goomba.gif")

        # create Mario - private instance variables
        self.player = self.__canvas.create_image(100, 350, image=self.imageMario) #will draw the image to however big it is

        self.enemiesList = []
        enemy1 = self.__canvas.create_image(500,350,image=self.imageGoomba)
        enemy2 = self.__canvas.create_image(300, 150, image=self.imageGoomba)
        enemy3 = self.__canvas.create_image(200,500, image=self.imageGoomba)

        self.enemiesList.append(enemy1)
        self.enemiesList.append(enemy2)
        self.enemiesList.append(enemy3)

        # create enemies - local variables

        # create enemyList - private instance variable

        # bind keyboard
        self.__canvas.bind("<Key>", self.key) # will allow for all of the different key functions to work
        # focus input on canvas
        self.__canvas.focus_set()

        # kick off the gameLoop
        self.gameLoop()

    # Sets up the key bindings
    def key(self, event):
        #code goes here
        if event.keysym == "Up":
            self.__canvas.move(self.player, 0, -20)
        elif event.keysym == "Down":
            self.__canvas.move(self.player,0, 20)
        elif event.keysym == "Left":
            self.__canvas.move(self.player, -20, 0)
        elif event.keysym == "Right":
            self.__canvas.move(self.player, 20, 0)
        self.__canvas.update()


    # Game Loop
    def gameLoop(self):

        self.goombaMovementCounter +=1

        # randomly move our enemies
        for enemy in self.enemiesList:
            moveX= (self.goombaMovementCounter % 21) - 10
            self.__canvas.move(enemy, moveX, 0)

            # Don't let the enemy go off the screen


        # Check for collisions
        coords = self.__canvas.bbox(self.player)
        collisionList = self.__canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3])

        for collision in collisionList:
            if collision in self.enemiesList:
                self.__canvas.delete(collision)#remove it from the screen

        # Don't let Mario go off the screen



        self.after(600, self.gameLoop)


def main():
    root = Tk()
    root.title("Mario Game")
    root.geometry("1000x700")
    app = Application(root)
    root.mainloop()

main()

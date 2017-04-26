
from tkinter import *


class Application(Frame):
    def __init__(self, root):
        #call PARENT constructor, AKA FRAME
        super().__init__(root)
        #Application inherits from Frame
        #Frame needs to call grid() to appear on the screen
        #therefore, Application also has to call grid
        self.grid()

        self.canvas = Canvas(self, width=800, height=700, bg="black")
        self.canvas.grid()

        self.player = self.canvas.create_rectangle(50,50,100,100, fill="white", outline="red")
        #when drawing shapes you don't have to call on grid

        self.greenOval = self.canvas.create_oval(500,300,700,400, fill="green")

        # we are going to connect the keyboard to a method
        # we push a key and a method will be called
        self.canvas.bind("<Key>", self.keyResponse)
        #tell python that our canvas sindow should be "Active"
        self.canvas.focus_set()

        self.gameLoop()

    def keyResponse(self, event):
        if event.keysym == "Up":
            self.canvas.move(self.player, 0, -30)
        elif event.keysym == "Down":
            self.canvas.move(self.player, 0, 30)
        elif event.keysym == "Right":
            self.canvas.move(self.player,30, 0)
        elif event.keysym == "Left":
            self.canvas.move(self.player, -30, 0)
        self.canvas.update() #to redraw the screen


    def gameLoop(self):
        # self.canvas.move(self.player, 5, 0)
        #we want this method to run again (aka call itself)
        coords = self.canvas.coords(self.player)
        if coords[0] >= 800:
            self.canvas.move(self.player, -850, 0)

        collisionList = self.canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3])

        for collision in collisionList: #collision is the variable/shape
            if collision != self.player:
                self.canvas.itemconfig(collision, fill="red", outline="blue")

        self.after(100, self.gameLoop)


def main():
    #create our main window
    root = Tk()
    root.title("Game_Example")
    root.geometry("800x700")
    app = Application(root)

    root.mainloop()

main()
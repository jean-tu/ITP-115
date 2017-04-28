from Story import Story
from tkinter import *
from tkinter import messagebox
from GUI import GUI

def main():

    root = Tk()
    root.title("Story Time")# set the title
    root.geometry("400x400")# set the size of the window
    root.configure() #Setting the background color
    # create a frame (AKA the cork board for the window, which is invisible when it is just itself)
    # frame = Frame(root)
    # make the frame appear on the screen
    # frame.grid()

    option = 1  # default to where they do mad libs instead of own
    play = True  # while the user still wants to play

    app = GUI(root)
    ##create the frame
    # print("\nWelcome to Story Time!")
    # while (play == True):
    #     # print("True")
    #     if option == 1:
    #         st = Story()
    #         print(st)
    #     play = False

    # start the program -- once you run this, nothing else after it will get called
    root.mainloop()

main()
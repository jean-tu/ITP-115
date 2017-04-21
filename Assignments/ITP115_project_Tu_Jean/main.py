from Story import Story
from tkinter import *
from tkinter import messagebox

def main():
    option = 1 #default to where they do mad libs instead of own
    play = True #while the user still wants to play

    root = Tk()
    # set the title
    root.title("Story Time")
    # set the size of the window
    root.geometry("1000x1000")

    # create a frame (AKA the cork board for the window, which is invisible when it is just itself)
    frame = Frame(root)
    # make the frame appear on the screen
    frame.grid()

    ##create the frame
    print("\nWelcome to Story Time!")
    while (play == True):
        # print("True")
        if option == 1:
            st = Story()
            print(st)
        play = False

    # start the program -- once you run this, nothing else after it will get called
    root.mainloop()

main()
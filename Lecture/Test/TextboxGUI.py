from tkinter import *
from GUI import GUI

def main():

    root = Tk()
    root.title("Story Time")# set the title
    root.geometry("400x400")# set the size of the window
    root.configure() #Setting the background color





    app = GUI(root)

    root.mainloop()

main()
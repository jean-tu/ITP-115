from tkinter import *

def main():
    #create the root window
    root = Tk()

    #set the title
    root.title("Hello World")

    #set the size
    root.geometry("500x500")


    #create a frame (AKA the cork board for the window, which is invisible when it is just itself)
    frame = Frame(root)
    #make the frame appear on the screen
    frame.grid()

    #make a label
    labelName = Label(frame, text="My name is Jean!", fg="#0000ff",  font=("Times 20"))
    labelName.grid() #is what puts it there in the grid
    labelPython = Label(frame, text="Python is super phun!", fg="#990000", bg="#ffcc00")
    labelPython.grid()
    labelFood = Label(frame, text="Everytime I ask students for food, they always say pizza!")
    labelFood.grid()

    buttonOrder = Button(frame, text="Order Amazon Fresh")
    buttonOrder.grid()

    entryFood = Entry(frame)
    entryFood.grid()

    #start the program -- once you run this, nothing else after it will get called
    root.mainloop()

main()
from tkinter import *
from tkinter import messagebox

class Pizza(Frame):
    def __init__(self, root):
        super().__init__(root)
        # messagebox.showinfo("Notice", "It is week 13!")
        # create all the widgets here
        # make a label
        self.labelName = Label(self, text="My name is Jean!", fg="#0000ff", font=("Times 20"))
        self.labelName.grid()  # is what puts it there in the grid
        self.labelPython = Label(self, text="Python is super phun!", fg="#990000", bg="#ffcc00")
        self.labelPython.grid()
        self.labelFood = Label(self, text="Everytime I ask students for food, they always say pizza!",\
                               font="Times 20")
        self.labelFood.grid()

        self.buttonOrder = Button(self, text="Order Amazon Fresh", fg="#990000", font="Times 20", \
                                  activeforeground="#FFFFFF", activebackground="#000000",
                                  command=self.orderFood)
        self.buttonOrder.grid()

        self.entryFood = Entry(self, fg="#990000", bg="#ffcc00", font="Calibri 20")
        self.entryFood.grid()

        self.buttonComplaint = Button(self, font="Calibri 20", text="Submit Complaint",
                                      command=self.fileComplaint)
        self.buttonComplaint.grid(row=0, column=1, rowspan=5)

        self.txtComplaint=Text(self, width=40, height=5, bg="#ffcc00")
        self.txtComplaint.grid(row=5, column=0, columnspan =2)

    def orderFood(self):
        """
            message box that says "Pasta is on its way"
            also, clear the entry box
        """
        order = self.entryFood.get()
        messagebox.showinfo("Fresh", str(order) + " food is on its way")
        self.entryFood.delete(0, END)

    def fileComplaint(self):
        response =  messagebox.askyesno("Complaint", "Are you really certain that is what you want to do?")
        if response == True:
            messagebox.showinfo("Complaint", "I'm terribly sorry about your service")
        else:
            messagebox.showinfo("Complaint", "I'm glad you changed your mind")

def main():
    #create the root window
    root = Tk()

    #set the title
    root.title("Hello World")

    #set the size
    root.geometry("500x500")


    #create a frame (AKA the cork board for the window, which is invisible when it is just itself)
    frame = Pizza(root)
    #make the frame appear on the screen
    frame.grid()



    #start the program -- once you run this, nothing else after it will get called
    root.mainloop()

main()
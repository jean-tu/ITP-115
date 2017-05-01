# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def hello():
    root = top
    root.title("HELLO")
    # entry = Entry(top, width=40)
    # messagebox.askquestion("Say Hello", entry)

B1 = Button(top, text = "Say Hello", command = hello)
# B1.place(x = 35,y = 50)
B1.grid()
top.mainloop()
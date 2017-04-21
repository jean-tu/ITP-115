# Superhero Battle

from tkinter import *
from Application import Application

def main():
    root = Tk()
    root.title("Superhero Battle")
    root.geometry("520x500")
    root.configure(background="#ffcc00")
    app = Application(root)
    root.mainloop()

# call main
main()
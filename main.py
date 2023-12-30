
from tkinter import *
root = Tk()
root.geometry("500x400")
f2 = Frame(root, bg="Black", borderwidth=8, relief=GROOVE)
f2.pack(side= TOP, fill="y")
l = Label(f2, text="WELCOME TO MY COLLEGE")
l.pack(padx=10)
f1 = Frame(root, bg="Black", borderwidth=8, relief=GROOVE)
f1.pack(side= TOP, fill="x")
l = Label(f1, text="LOKMANYA TIKAK COLLEGE OF ENGINEERING")
l.pack(pady=10)
root.mainloop()


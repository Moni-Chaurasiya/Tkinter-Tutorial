from tkinter import *
root = Tk()
root.geometry("500x400")
root.title("Bhayanak Pari Ka Kala Calculator")
def first():
    print("Addition")

def second():
    print("Subtraction")

def third():
    print("Multiplication")

def forth():
    print("Division")

frame = Frame(root, bg="Black", borderwidth=8, relief=GROOVE)
frame.pack(side= TOP, fill="x")
l = Label(frame, text="CLICK ON BUTTON")
l.pack(pady=10)
f1 = Frame(root, bg="blue", borderwidth=8, relief=GROOVE)
f1.pack(side= TOP, fill="x")
b1 = Button(f1, text="+", fg="Black", command= first)
b1.pack(side=LEFT)
b1 = Button(f1, text="-", fg="Black", command= second)
b1.pack(side=LEFT)
b1 = Button(f1, text="*", fg="Black", command= third)
b1.pack(side=LEFT)
b1 = Button(f1, text="/", fg="Black", command= forth)
b1.pack(side=LEFT)
root.mainloop()
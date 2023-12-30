from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("1000x600")
root.title("My Menu")
def myfunc():
    print("I am a Function")

def help():
    print("I will help you")
    tmsg.showinfo("help", "Moni will help you")


def rate():
    print("Rate us")
    value= tmsg.askquestion("How was your experience","You used my GUI")
    if value =="yes":
        msg="Great"
    else:
        msg="what went wrong"
        tmsg.showinfo("Experience",msg)

#mymenu = Menu(root)
#mymenu.add_command(label="File", command=myfunc)
#mymenu.add_command(label="Exit", command=quit)
#root.config(menu=mymenu)

mymenubar = Menu(root)
m1 = Menu(mymenubar, tearoff=0)
m1.add_command(label="New Project",command=myfunc)
m1.add_command(label="save",command=myfunc)
m1.add_command(label="save as",command=myfunc)
m1.add_separator()
m1.add_command(label="print",command=myfunc)
root.config(menu=mymenubar)

mymenubar.add_cascade(label="File",menu=m1)


m2 = Menu(mymenubar, tearoff=0)
m2.add_command(label="copy",command=myfunc)
m2.add_command(label="cut",command=myfunc)
m2.add_command(label="paste",command=myfunc)
m2.add_separator()
m2.add_command(label="find",command=myfunc)
root.config(menu=mymenubar)

mymenubar.add_cascade(label="Edit",menu=m2)

m3 = Menu(mymenubar, tearoff=0)
m3.add_command(label="help",command=help)
m3.add_command(label="rate us",command=rate)
mymenubar.add_cascade(label="help",menu=m3)
root.config(menu=mymenubar)


root.mainloop()

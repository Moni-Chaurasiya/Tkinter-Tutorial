from tkinter import *
#import tkinter.messagebox as tmsg
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

i=0

root=Tk()
root.geometry("1000x600")
root.title("ListBox")
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First item of our list box")
Button(root, text="Add Item", command=add).pack()

root.mainloop()
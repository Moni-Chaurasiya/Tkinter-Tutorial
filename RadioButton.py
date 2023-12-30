from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("1000x600")
root.title("Radio Button")
def order():
    tmsg.showinfo("Order Received",f"We have received your order for {var.get()}.Thanks for ordering")

var = IntVar()
#var.set(1)
Label(root, text="What would you like to have Moni?",font="Times 20 bold",).pack()
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value=1).pack(anchor="w")
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value=2).pack(anchor="w")
radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value=3).pack(anchor="w")
radio=Radiobutton(root,text="PaniPuri",padx=14,variable=var,value=4).pack(anchor="w")
Button(text="Order Now",command=order).pack()
root.mainloop()
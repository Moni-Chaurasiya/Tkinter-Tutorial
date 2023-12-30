from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("1000x600")
root.title("Slider")
def getrupees():
    print(f"We have credited{myslider2.get()} rupees to your bank account")
    tmsg.showinfo("Amount Credited!",f"We have credited{myslider2.get()} rupees to your bank account")

#myslider = Scale(root, from_=0, to=100)
#myslider.pack()
Label(root,text="How many rupees you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL,tickinterval=5)
myslider2.set(34)
myslider2.pack()
Button(root, text="Get rupees", command=getrupees).pack()
root.mainloop()
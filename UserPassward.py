from tkinter import *
def getvals():

    print(uservalue.get())
    print(passvalue.get())

root = Tk()
root.geometry("500x400")
root.title("Username and Passward")
user = Label(root, text="username")
passward = Label(root, text="passward")
user.grid()
passward.grid(row=1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="SUMIT",command=getvals).grid()

root.mainloop()
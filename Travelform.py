from tkinter import *
def getvals():
    print("Your response is submitted")
    print(f"{namevalue.get(), agevalue.get(), gendervalue.get(), phonevalue.get(), paymentmodevalue.get(),foodservicevalue.get()}")

    with open("blank.txt","a")as f:
        f.write(f"{namevalue.get(), agevalue.get(), gendervalue.get(), phonevalue.get(), paymentmodevalue.get(),foodservicevalue.get()}")
root = Tk()
root.title("Sherkhan tak ka safer")
root.geometry("500x400")
Label(root, text="WELCOME TO BHAYANAKLOK", font="Times 25 bold italic", bg="grey", fg="Black").grid(row=0, column=1)


name = Label(root, text="Name")
age = Label(root, text="Age")
gender = Label(root, text="Gender")
phone = Label(root, text="phone")
paymentmode = Label(root, text="Payment Mode")


name.grid(row=1, column=1)
age.grid(row=2, column=1)
gender.grid(row=3, column=1)
phone.grid(row=4, column=1)
paymentmode.grid(row=5, column=1)

namevalue = StringVar()
agevalue = StringVar()
gendervalue = StringVar()
phonevalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable = namevalue)
ageentry = Entry(root, textvariable = agevalue)
genderentry = Entry(root, textvariable = gendervalue)
phoneentry = Entry(root, textvariable = phonevalue)
paymentmodeentry = Entry(root, textvariable = paymentmodevalue)

nameentry.grid(row=1, column=2)
ageentry.grid(row=2, column=2)
genderentry.grid(row=3, column=2)
phoneentry.grid(row=4, column=2)
paymentmodeentry.grid(row=5, column=2)

foodservice = Checkbutton(text="Want to prebook your meal", variable = foodservicevalue)
foodservice.grid(row=6, column=2)

Button(text="Submit to Bhayanak travels",command=getvals).grid(row=7, column=2)


root.mainloop()
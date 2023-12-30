from tkinter import *
from PIL import Image, ImageTk

imaginary_calsi_root = Tk()

imaginary_calsi_root.geometry("644x434")
imaginary_calsi_root.minsize(200,100)
imaginary_calsi_root.maxsize(1200,988)
# photo = PhotoImage(file="record.txt")
# For Jpg Images
image = Image.open("Image.png")
photo = ImageTk.PhotoImage(file="Image.png")


moni_label=Label(image=photo)
moni_label.pack()


imaginary_calsi_root.mainloop()
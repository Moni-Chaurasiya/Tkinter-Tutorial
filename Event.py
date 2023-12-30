from tkinter import *

def Moni(event):
    print(f"You clicked on the button at {event.x},{event.y}")
root = Tk()
root.title("Bhayanakpari ka GUI")
root.geometry("1000x500")
widget = Button(root, text="click me please")
widget.pack()

widget.bind('<Button-1>', Moni)
widget.bind('<Double-1>', quit)
root.mainloop()
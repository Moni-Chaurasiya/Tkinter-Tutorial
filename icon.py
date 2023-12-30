from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Moni ka GUI")
#root.wm_iconbitmap("1.ico")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height})

root.mainloop()
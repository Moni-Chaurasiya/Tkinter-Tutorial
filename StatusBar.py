from tkinter import *
root = Tk()
root.geometry("1000x600")
root.title("ScrollBar")
def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")
statusvar = StringVar()
statusvar.set("Ready")
sbar=Label(root, textvariable=statusvar,relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Upload", command=upload).pack()

root.mainloop()
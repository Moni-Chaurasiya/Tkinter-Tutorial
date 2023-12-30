from tkinter import *
root = Tk()
root.geometry("1000x600")
root.title("ScrollBar")
#For connecting ScrollBar to a widget
#1. Widget(yscrollcommand = scrollbar.set)
#2. scroll.config(command=widget.yview)
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
listbox = Listbox(root, yscrollcommand= scrollbar.set)
for i in range(346):
    listbox.insert(END, f"Item{i}")
listbox.pack(fill="both",padx=22)
scrollbar.config(command=listbox.yview)







root.mainloop()


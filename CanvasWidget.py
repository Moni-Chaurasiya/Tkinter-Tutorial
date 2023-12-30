from tkinter import *

root = Tk()
root.title("Moni ka GUI")

canvas_width = 1000
canvas_height = 500

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()
can_widget.create_line(0, 250, 1000, 250, fill="Blue")
#can_widget.create_line(1000, 500, 0, 0, fill="Blue")
can_widget.create_rectangle(480,230,520,270,fill="pink")
can_widget.create_text(500,250,text="Moni")
can_widget.create_oval(480,230,520,270)


root.mainloop()
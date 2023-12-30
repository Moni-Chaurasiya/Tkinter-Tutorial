from tkinter import *
root=Tk()
root.geometry("1400x1000")
root.title("My GUI With Moni")

title_label = Label(text ='''
My name is Moni Chaurasiya.
\nCurrently I am in my second year of engineering and I know C, C++, Python language.
\nI am aspiring, hardworking, consistent and a quick learner.
\nI am also interested in learning new technologies.
\nI am very organized and responsible who can be trusted to do any given task with accuracy and perfection.
\nCoding is something I like to do everyday and I am always looking for new projects to work on.''', bg="blue",
fg="white", padx=13, pady=50, font="Times 18 bold italic", borderwidth=6 ,relief=SUNKEN
                    )
title_label.pack(side=TOP,anchor="se",fill=X)
title_label.pack(side=LEFT,fill=Y,padx=35,pady=35)
root.mainloop()

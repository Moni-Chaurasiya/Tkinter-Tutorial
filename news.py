from tkinter import *
root = Tk()
root.geometry("1500x1000")
root.title("My GUI With Moni")
root.minsize(200,100)
root.maxsize(1500,1000)
title_label= Label(text ='''
TIMES OF INDIA''', bg="Grey", fg="Black", font="Times 25 bold italic", borderwidth = 6 ,relief=SUNKEN
)
title_label.pack(side=TOP,fill=X)
#photo = PhotoImage(file="record.txt")
#moni_label=Label(image=photo, )
#moni_label.pack(side=TOP,fill=X)
Soni_label = Label(text ='''
My name is Moni Chaurasiya.
\nCurrently I am in my second year of engineering and I know C, C++, Python language.
\nI am aspiring, hardworking, consistent and a quick learner.
\nI am also interested in learning new technologies.
\nI am very organized and responsible who can be trusted to do any given task with accuracy and perfection.
\nCoding is something I like to do everyday and I am always looking for new projects to work on.''', bg="blue",
fg="white", padx=3, pady=5, font="Times 18 bold italic", borderwidth=6 ,relief=SUNKEN
                    )
Soni_label.pack(side=TOP,anchor="se",fill=X)
Soni_label.pack(side=LEFT,fill=Y,padx=3,pady=5)
root.mainloop()

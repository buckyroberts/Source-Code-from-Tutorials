from tkinter import *

root = Tk()

photo = PhotoImage(file="banana.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()

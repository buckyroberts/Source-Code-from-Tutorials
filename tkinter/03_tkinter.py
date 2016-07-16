from tkinter import *

root = Tk()

one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X)  # fill=X - makes the widget as wide as the parent
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)

root.mainloop()

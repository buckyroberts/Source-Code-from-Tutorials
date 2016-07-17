from tkinter import *

root = Tk()

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

# widgets centered by default, sticky option to change
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

# widgets can take up more than one cell with columnspan and rowspan
c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

root.mainloop()

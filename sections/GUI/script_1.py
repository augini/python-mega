from tkinter import *
from tkinter import messagebox

window = Tk()

# Define a function to show the popup message
def km_to_miles():
   miles = int(e1_value.get()) * 1.6
   t1.insert(END, miles)
   
b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0,column=1)

t1=Text(window)
t1.grid(row=0, column=2)

window.mainloop()
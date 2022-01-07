import tkinter
from tkinter import *



root = tkinter.Tk()
root.title("AutoCompletion")
root.geometry("300x300")
lb1= Label(root)
lb1.config(text= "Enter incomplete word")
lb1.pack(pady= 30, ipady = 10 , ipadx = 10)

e1 = Entry(root)
e1.pack(ipady = 5 , ipadx = 5)

root.mainloop()
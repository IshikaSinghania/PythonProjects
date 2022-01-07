import tkinter
from tkinter import *
import random
from tkinter import messagebox
from random import shuffle


# Including words to be used for the game
answers=["python","google","random","corona","youtube","gmail","hotmail","game","words","samosa","india"]

words=[]

for i in answers:
    word=list(i)
    shuffle(word)
    words.append(word)

num =random.randint(0,len(words)-1)



def initial():
    global words,answers,num
    lb1.config(text = words[num])

# Checking if answer is right or wrong
def ans_check():
    global words,num,answers
    user_input=e1.get()
    if user_input==answers[num]:
        messagebox.showinfo("SUCCESS","Right Answer")
        reset()
    else:
         messagebox.showinfo("Error","Wrong Answer")
         e1.delete(0,END)


def reset():
    global words,num,answers
    num =random.randint(0,len(words))
    lb1.configure(text=words[num])
    e1.delete(0,END)
    
# creating GUI
root = tkinter.Tk()
root.title("Jumble Word Game")
root.geometry("300x300")
lb1 = Label(root, font = 'times 20')
lb1.pack(pady= 30, ipady = 10 , ipadx = 10)

answer= StringVar()
e1 = Entry(root,textvariable = answer)
e1.pack(ipady = 5 , ipadx = 5)

buttton1= Button(root,text="Check", width = 20 , command=ans_check)
buttton1.pack(pady=40)

buttton2= Button(root,text="Reset", width = 20 , command=reset)
buttton2.pack()

initial()
root.mainloop()


from tkinter import *

from numpy import equal, number

root=Tk()

root.title("Calculator")

num=IntVar()


e=Entry(textvariable=num,fg="black",width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)

def press(num):
    r=e.get()
    e.delete(0,END)
    e.insert(0,r+str(num))
    
def add():
    fnum=e.get()
    global numm
    numm=int(fnum)
    e.delete(0,END)


def clear():
    e.delete(0,END)
    
    
def Equal():
    sum=e.get()
    e.delete(0,END)
    e.insert(0,numm+int(sum))


Button(text="9",font=12,fg="black",padx=20,command=lambda:press(9)).grid(row=1,column=0)
Button(text="8",font=12,fg="black",padx=20,command=lambda:press(8)).grid(row=1,column=1)
Button(text="7",font=12,fg="black",padx=20,command=lambda:press(7)).grid(row=1,column=2)
Button(text="6",font=12,fg="black",padx=20,command=lambda:press(6)).grid(row=2,column=0)
Button(text="5",font=12,fg="black",padx=20,command=lambda:press(5)).grid(row=2,column=1)
Button(text="4",font=12,fg="black",padx=20,command=lambda:press(4)).grid(row=2,column=2)
Button(text="3",font=12,fg="black",padx=20,command=lambda:press(3)).grid(row=3,column=0)
Button(text="2",font=12,fg="black",padx=20,command=lambda:press(2)).grid(row=3,column=1)
Button(text="1",font=12,fg="black",padx=20,command=lambda:press(1)).grid(row=3,column=2)
#Button(text="clr",font=12,fg="black",padx=20,command=clear).grid(row=4,column=0)
Button(text="0",font=12,fg="black",padx=20,command=lambda:press(0)).grid(row=4,column=1)
#Button(text="=",font=12,fg="black",padx=20,command=Equal).grid(row=4,column=2)
#Button(text="+",font=12,fg="black",padx=20,command=add).grid(row=5,column=1)




root.mainloop() 
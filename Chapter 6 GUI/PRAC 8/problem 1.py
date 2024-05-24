from ast import Num
from cProfile import label
from distutils.command import config
from logging import root
from tkinter import *

screen=Tk()

screen.geometry("720x480")


Num1=IntVar()
Num2=IntVar()


def sum():
    summ=Num1.get() + Num2.get()
    output.config(text="the sum of "+str(Num1.get())+ " + " +str(Num2.get()) +" is "+ str(summ))

    
Label(screen,text="num1",fg="blue",font=12,).grid(row=1,column=1)
Label(screen,text="num2",fg="blue",font=12,).grid(row=2,column=1)
Entry(screen,textvariable=Num1,fg="blue",bg="gray").grid(row=1,column=2)
Entry(screen,textvariable=Num2,fg="blue",bg="gray").grid(row=2,column=2)
Button(screen,text="summ",fg="black",bg="silver",command=sum).grid(row=3,column=2)
output=Label(screen, fg="blue",bg="silver",font=14,width=25,height=4)
output.grid(row=4,column=2)
screen.mainloop()
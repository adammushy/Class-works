from tkinter import *
#find th summ of the 7,9,4 and 5

from tkinter import *
from turtle import width

screen=Tk()
screen.geometry("720x480")
#method 1 4 enrty n labels with 1empty label
num1=IntVar()
num4=IntVar()
num3=IntVar()
num2=IntVar()

def on_click():
    summ= num1.get()+num1.get()+num1.get()+num1.get()
    print("the sum of the 4 num is ",summ)
    empty.config(text="the sum of four numbers is "+ str(summ))

Label(screen, text="1st num",fg="black",width=15).grid(row=0,column=0)
Label(screen, text="2nd num",fg="black",width=15).grid(row=1,column=0)
Label(screen, text="3rd num",fg="black",width=15).grid(row=2,column=0)
Label(screen, text="4th num",fg="black",width=15).grid(row=3,column=0)
Entry(screen,textvariable=num1,fg="black",width=15,borderwidth=4).grid(row=0,column=1)
Entry(screen,textvariable=num2,fg="black",width=15,borderwidth=4).grid(row=1,column=1)
Entry(screen,textvariable=num3,fg="black",width=15,borderwidth=4).grid(row=2,column=1)
Entry(screen,textvariable=num4,fg="black",width=15,borderwidth=4).grid(row=3,column=1)
Button(screen, text="Click",fg="black",width=15,bg="red",command=on_click).grid(row=5,column=2)

empty=Label(screen,fg="black",width=25,height=5)
empty.grid(row=4,column=2)




screen.mainloop()
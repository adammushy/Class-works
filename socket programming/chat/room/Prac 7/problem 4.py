from cgitb import text
from tkinter import *

screen=Tk()

screen.geometry("250x200+50+50")

screen.title("Add Numbers")


Num1=IntVar()
Num2=IntVar()


def Operation():
    Label(screen,text="num1",fg="blue",font=12,).grid(row=1,column=1)
    Label(screen,text="num2",fg="blue",font=12,).grid(row=2,column=1)
    Entry(screen,textvariable=Num1,fg="blue",bg="gray").grid(row=1,column=2)
    Entry(screen,textvariable=Num2,fg="blue",bg="gray").grid(row=2,column=2)
   
    output=Label(screen, fg="blue",bg="silver",font=14,width=25,height=4)
    output.grid(row=4,column=2)
    def Sum():
        x=Num1.get()
        y=Num2.get()
        sum=x+y
        output.config(text="the sum is "+ str(sum))
        print("the sum is ", sum)
    Button(screen,text="Add",fg="black",bg="blue",command=Sum).grid(row=3,column=3)
     
Button(screen,text="start",fg="black",bg="blue",font=12,command=Operation).grid(row=0,column=3)


screen.mainloop()
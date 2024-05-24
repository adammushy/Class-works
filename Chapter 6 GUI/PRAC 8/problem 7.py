from tkinter import *

from numpy import number

screen=Tk()

screen.title("Calculator")

number=IntVar()

e=Entry(screen,textvariable=number,font=12,fg="black",width=25)
e.grid(row=0,column=0,columnspan=10) 


screen.mainloop()
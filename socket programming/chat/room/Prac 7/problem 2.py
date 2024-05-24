from turtle import Screen, width
from numpy import fromfile


from tkinter import *

screen=Tk()
screen.geometry("720x480")
screen.title("GUI")

Age=IntVar()
full_name=StringVar()

Label(screen,text="Age:",fg="black",font=14,).grid(row=1,column=1)
Label(screen,text="Full name:",fg="black",font=14,).grid(row=2,column=1)
Entry(screen,font=12,textvariable=Age,width=20,borderwidth=5).grid(row=1,column=2)
Entry(screen,font=12,textvariable=full_name,width=20,borderwidth=5).grid(row=2,column=2)






screen.mainloop()
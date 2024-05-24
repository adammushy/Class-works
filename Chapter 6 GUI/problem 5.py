from tkinter import *
from tokenize import Name

screen=Tk()

screen.geometry("350x250+100+100")
screen.title("My Name")
Name=StringVar()

def Cout():
    name=Name.get()
    print("my name is",name)
    display.config(text="my name is "+ name)
    
    
Label(screen,text="Name",fg="blue",font=14).grid(row=1,column=1)
Entry(screen,textvariable=Name,fg="blue",bg="silver",font=14).grid(row=1,column=2)


Button(screen,text="print my name",command=Cout).grid(row=2,column=2)

display=Label(screen,fg="blue",bg="gray",width=20,height=4,pady=20,padx=15)
display.grid(row=3,column=2)

screen.mainloop()

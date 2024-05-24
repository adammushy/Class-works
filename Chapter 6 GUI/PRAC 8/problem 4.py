from tkinter import *



screen=Tk()

screen.title("Calculator")

number=IntVar()


e=Entry(screen,textvariable=number,fg="black",width=30,borderwidth=5)
e.grid(row=0,column=0,columnspan=10)
def click(number):
    r=e.get()
    e.delete(0,END)
    e.insert(0,r+str(number))

def add():
    fnum=e.get()
    global num
    num=int(fnum)   
    e.delete(0,END)
    

def clear():
    e.delete(0,END)
    
def equal():
    snum=e.get()
    e.delete(0,END)
    e.insert(0,num+int(snum))


Button(text="7",fg="black",font=12,padx=25,command=lambda:click(7)).grid(row=1,column=0)
Button(text="8",fg="black",font=12,padx=25,command=lambda:click(8)).grid(row=1,column=1)
Button(text="9",fg="black",font=12,padx=25,command=lambda:click(9)).grid(row=1,column=2)
Button(text="4",fg="black",font=12,padx=25,command=lambda:click(4)).grid(row=2,column=0)
Button(text="5",fg="black",font=12,padx=25,command=lambda:click(5)).grid(row=2,column=1)
Button(text="6",fg="black",font=12,padx=25,command=lambda:click(6)).grid(row=2,column=2)
Button(text="3",fg="black",font=12,padx=25,command=lambda:click(3)).grid(row=3,column=0)
Button(text="2",fg="black",font=12,padx=25,command=lambda:click(2)).grid(row=3,column=1)
Button(text="1",fg="black",font=12,padx=25,command=lambda:click(1)).grid(row=3,column=2)
Button(text="0",fg="black",font=12,padx=25,command=lambda:click(0)).grid(row=4,column=0)

Button(text="+",fg="black",font=12,padx=25,command=add).grid(row=5,column=0)
Button(text="=",fg="black",font=12,padx=25,command=equal).grid(row=5,column=1)

Button(text="clear",fg="black",font=12,padx=25,command=clear).grid(row=4,column=1)






screen.mainloop()
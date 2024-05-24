from tkinter import *

root = Tk()#1.create frame
root.title("calculator")

#to include component in the frame
number= IntVar()

e=Entry(root,textvariable = number,font =12,fg="blue" ,width= 30,borderwidth=10)
e.grid(row=0,column=0,columnspan=3)

def click(number):
    r = e.get()
    e.delete(0,END)
    e.insert(0,r+str(number))
    
def clear():
    e.delete(0,END)


def add():
    fnum = e.get()
    global num
    num =int(fnum)
    e.delete(0,END)

def equal():
    snum =e.get()
    e.delete(0,END)
    e.insert(0,num+int(snum))


Button(text = "7",font =12,fg="blue",padx=20,command=lambda:click(7)).grid(row=1,column=0)
Button(text = "4",font =12,fg="blue",padx=20,command=lambda:click(4)).grid(row=1,column=1)
Button(text = "5",font =12,fg="blue",padx=20,command=lambda:click(5)).grid(row=1,column=2)
Button(text = "9",font =12,fg="blue",padx=20,command=lambda:click(9)).grid(row=2,column=2)
Button(text = "+",font =12,fg="blue",padx=20,command=add).grid(row=2,column=1)
Button(text = "=",font =12,fg="blue",padx=20,command=equal).grid(row=2,column=0)
Button(text = "clear",font =12,fg="blue",padx=20,command=clear).grid(row=3,column=0)
#Button(text = "9",font =12,fg="blue",padx=20,command=lambda:click(9)).grid(row=2,column=0)





root.mainloop()
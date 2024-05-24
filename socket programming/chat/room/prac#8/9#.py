from tkinter import *

root=Tk()
root.geometry("300x300")

number=IntVar()

def onclick(number):
    e.delete(0,END)
    e.insert(0,str(number))
    
def add():
    fnum=e.get()
    global num1
    global select
    select="+"
    num1=int(fnum)
    e.delete(0,END)
def clear():
    e.delete(0,END)
def equal():
    snum=e.get()
    e.delete(0,END)
    if(select=="+"):
        sum=num1+int(snum)
        e.insert(0,sum)
        el.config(text="the sum is "+str(sum))

el=Label(root,font=15,fg='black')
el.grid(row=7,column=0)
e=Entry(root,textvariable=number,borderwidth=10,width=48)
e.grid(row=0,column=0,columnspan=3)
Button(root,text='7',command=lambda:onclick(7),padx=40).grid(row=1,column=0)
Button(root,text='6',command=lambda:onclick(6),padx=40).grid(row=2,column=0)

Button(root,text='3',command=lambda:onclick(3),padx=40).grid(row=3,column=0)
Button(root,text='0',command=lambda:onclick(0),padx=40).grid(row=4,column=0)
Button(root,text='+',command=add,padx=40).grid(row=5,column=0)
Button(root,text='4',command=lambda:onclick(4),padx=40).grid(row=1,column=1)
Button(root,text='5',command=lambda:onclick(5),padx=40).grid(row=2,column=1)
Button(root,text='2',command=lambda:onclick(2),padx=40).grid(row=3,column=1)
Button(root,text='clr',command=clear,padx=90).grid(row=4,column=1,columnspan=2)
Button(root,text='=',command=equal,padx=40).grid(row=5,column=1)
Button(root,text='9',command=lambda:onclick(9),padx=40).grid(row=1,column=2)
Button(root,text='4',command=lambda:onclick(4),padx=40).grid(row=2,column=2)
Button(root,text='1',command=lambda:onclick(1),padx=40).grid(row=3,column=2)



root.mainloop()

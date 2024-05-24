from tkinter import *

root=Tk()
root.geometry("300x300")
def area():
    area=l.get()*w.get()
    e.config(text="the  area is "+str(area))
l=IntVar()
w=IntVar()
Label(root,text='enter the width',font=13,fg='blue').grid(row=0,column=0)
Label(root,text='enter the length',font=13,fg='blue').grid(row=1,column=0)

Entry(root,textvariable=w).grid(row=0,column=1)
Entry(root,textvariable=l).grid(row=1,column=1)

Button(root,text='click me',command=area).grid(row=2,column=1)
e=Label(root,font=13,fg='blue')
e.grid(row=3,column=1)


root.mainloop()

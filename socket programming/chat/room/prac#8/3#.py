from tkinter import *
root=Tk()
root.geometry("300x300")
text=StringVar()
def cl():
    e.config(text=text.get())
Entry(root,textvariable=text).grid(row=0,column=0)
Button(root,text='click me',command=cl).grid(row=1,column=0)

e=Label(root,font=13,fg='black')
e.grid(row=2,column=0)
root.mainloop()

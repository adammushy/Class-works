from tkinter import *
root=Tk()
root.geometry("300x300")
number=IntVar()
Entry(root,textvariable=number,borderwidth=10,width=48).grid(row=0,column=0,columnspan=3)
Button(root,text='7',padx=40).grid(row=1,column=0)
Button(root,text='6',padx=40).grid(row=2,column=0)
Button(root,text='3',padx=40).grid(row=3,column=0)
Button(root,text='0',padx=40).grid(row=4,column=0)
Button(root,text='+',padx=40).grid(row=5,column=0)
Button(root,text='8',padx=40).grid(row=1,column=1)
Button(root,text='5',padx=40).grid(row=2,column=1)
Button(root,text='2',padx=40).grid(row=3,column=1)
Button(root,text='clear',padx=90).grid(row=4,column=1,columnspan=2)
Button(root,text='=',padx=40).grid(row=5,column=1)
Button(root,text='9',padx=40).grid(row=1,column=2)
Button(root,text='4',padx=40).grid(row=2,column=2)
Button(root,text='1',padx=40).grid(row=3,column=2)



root.mainloop()

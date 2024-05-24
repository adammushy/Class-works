from tkinter import *

root = Tk()

root.title("Add Numbers")
root.geometry("400x300")
Label(root,text = "enter first number",font =10,fg ="blue",width =14,borderwidth = 5).grid(row = 0,column =0)
Label(root,text = "enter second number",font =10,fg ="blue",width =16,borderwidth = 5).grid(row = 1,column =0)
Label(root,text = "enter third number",font =10,fg ="blue",width =16,borderwidth = 5).grid(row = 2,column =0)
Label(root,text = "enter fourth number",font =10,fg ="blue",width =16,borderwidth = 5).grid(row = 3,column =0)
emptyLabel=Label(root,font =10,fg ="blue",width =16,borderwidth = 5)
emptyLabel.grid(row = 4,column =1)
number1 =IntVar()
e1= Entry(root,textvariable =number1,font = 10,fg ="blue",width = 10,borderwidth = 5)
e1.grid(row =0,column = 1)
number2 =IntVar()
e2= Entry(root,textvariable =number2,font = 10,fg ="blue",width = 10,borderwidth = 5)
e2.grid(row =1,column = 1)
number3=IntVar()
e3= Entry(root,textvariable =number3,font = 10,fg ="blue",width = 10,borderwidth = 5)
e3.grid(row =2,column = 1)
number4 =IntVar()
e4= Entry(root,textvariable =number4,font = 10,fg ="blue",width = 10,borderwidth = 5)
e4.grid(row =3,column = 1)

def on_click():
    Sum =number1.get()+number2.get()+number3.get()+number4.get()
    emptyLabel.config(text="the sum is  "  + str(Sum))
    print("the sum is " ,Sum)

Button(text = "clik",font =12,fg="blue",padx=20,command=on_click).grid(row =5,column=1)
root.mainloop()


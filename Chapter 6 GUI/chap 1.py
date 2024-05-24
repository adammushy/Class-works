import tkinter

# from turtle import width

# from setuptools import Command

mastra=Tk() #
mastra.title("Area of Rectangle")
mastra.geometry("640x400")

length=IntVar()
width=IntVar()
def  Area():
    area= length.get() * width.get()
    '''
    print("the area is :: ",area)'''
    empty_label.config(text="the area is :: "+str(area))# to print the answer on the root window  on your prog
    print("the area is :: ",area)
Label(mastra,text="Length",font=12, fg="blue" ,width=12,borderwidth=5).grid(row=0,column=0)
Label(mastra,text="width",font=12, fg="blue" ,width=12,borderwidth=5).grid(row=1,column=0)

Entry(mastra,font=12,textvariable=length, fg="blue",width=10,borderwidth=5).grid(row=0,column=1)
Entry(mastra,textvariable=width, font=12, fg="blue",width=10,borderwidth=5).grid(row=1,column=1)

Button(mastra,text="Calculate",fg="white",bg="blue",font=12,width=8 ,command=Area).grid(row=2,column=1 )
empty_label=Label(mastra,font=12, fg="blue",bg="white" ,width=25, height=5,borderwidth=5)
empty_label.grid(row=3,column=1)




mastra.mainloop()
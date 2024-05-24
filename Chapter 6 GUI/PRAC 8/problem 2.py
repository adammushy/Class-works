from pydoc import text
from tkinter import *

screen=Tk()
screen.geometry("720x480")
screen.title("Area")

length=IntVar()
width=IntVar()
def arearect():
   area=length.get() * width.get() 
   print("the area is "+ str(area))
   answersheet.config(text="the area is "+str(area))
   
   
   


Label(screen, text="Enter length",font=14,fg="blue").grid(row=1,column=1)
Label(screen, text="Enter width",font=14,fg="blue").grid(row=2,column=1)
Entry(screen, textvariable=length,font=14,fg="blue",bg="gray",width=15).grid(row=1,column=2)
Entry(screen, textvariable=width,font=14,fg="blue",bg="gray",width=15).grid(row=2,column=2)
Button(screen,text="calculate",font=14,bg="red",width=12,command=arearect).grid(row=3,column=2)

answersheet=Label(screen,fg="red",bg="gray",width=30,height=4)
answersheet.grid(row=4,column=2)




screen.mainloop()
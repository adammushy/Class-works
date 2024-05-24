#the user interact with a set of visual controls such as butons,labels,boxes,tool bars,menu items etc
#here the user interact with machine

import tkinter
from tkinter import *

'''root = Tk()
#creating a label widget
mylabel = Label(root, text="hello world")# this is widget

#showing it into the screen

mylabel.pack() 

root.mainloop()'''

root = Tk() #created a window
root.title("Welcome at DIT")# the title ofwindow

root.geometry("720x480+200+200")#the size od  THE + indicate the window to shift by those pixel w.r.t to sides
Label(root,text="Age:",font="Arial 14 ",fg="blue",width=5 ).grid(row=0, column=0)

age = IntVar()
Entry(root,textvariable=age,font="Arial 14 ",fg="blue",width=20,borderwidth=5 ).grid(row=0,column=1)
def Age():
    print("my age is ",age.get())    

Button(root,text="click age",font=12, fg="white",bg="black",padx=20,pady=2,command=Age).grid(row=3,column=1, sticky=E)#padx or pady used to size the button is u
#you cant use grid and pack if grid is used from start you can't use grid
#sticky is used to put or align an the button to a certain side and it is used inside pack or pace or grid

'''
Label(root,text="1.Telecom ",font="Arial 12 ",fg="black").place(x=45,y=30)#by using place we put wher we want it to be
Label(root,text="2.Computer ",font="Arial 12 ",fg="black").place(x=45,y=50)#by using place we put wher we want it to be
'''

root.mainloop() # object of main class is accessed by  mainloop
 
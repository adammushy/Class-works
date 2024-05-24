
from tkinter import *
from tokenize import Floatnumber

from cv2 import borderInterpolate
from numpy import multiply

root=Tk()
root.title("Calculator")

e=Entry(root,width=40,borderwidth=5)

e.insert(0,"")
e.grid(row=0,column=0,columnspan=3,padx=5,pady=5) #column span indicate number of column it can span to based on the entry
#padx ppady make entry or button look bigger accordingly

def button_add(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+ str(number))
    
def equal(): 
    snum=e.get()
    e.delete(0,END)
    if math=="addition":
        ans=fnum+int(snum)
        e.insert(0,ans)
    elif math=="subtract":
        ans=fnum-int(snum)
        e.insert(0,ans)
    elif math=="multiply":
        ans=fnum*int(snum)
        e.insert(0,ans)
    elif math=="division":
        ans=fnum/int(snum)
        e.insert(0,float(ans))

def clear():
    e.delete(0,END)

def add():
    num=e.get()
    global fnum
    global math
    math="addition"
    fnum=int(num)
    e.delete(0,END)
    
def subtract():
    num=e.get()
    global fnum
    global math
    fnum=int(num)
    e.delete(0,END)
    math="subtract"
    
    
def times():
    num=e.get()
    global fnum
    global math
    fnum=int(num)
    e.delete(0,END)
    math="multiply"
    
def divide():
    num=e.get()
    global fnum
    global math
    math="addition"
    fnum=int(num)
    e.delete(0,END)
    math="division"




button1= Button(root,text="1",padx=30,pady=15,command=lambda:button_add(1))
button2= Button(root,text="2",padx=30,pady=15,command=lambda:button_add(2))
button3= Button(root,text="3",padx=30,pady= 15,command=lambda:button_add(3))
button4= Button(root,text="4",padx=30,pady=15,command=lambda:button_add(4))
button5= Button(root,text="5",padx=30,pady=15,command=lambda:button_add(5))
button6= Button(root,text="6",padx=30,pady=15,command=lambda:button_add(6))
button7= Button(root,text="7",padx=30,pady=15,command=lambda:button_add(7))
button8= Button(root,text="8",padx=30,pady=15,command=lambda:button_add(8))
button9= Button(root,text="9",padx=30,pady=15,command=lambda:button_add(9))
button_equal= Button(root,text="=",padx=30,pady=15,command=equal)
buttonadd= Button(root,text="+",padx=30,pady=15,command=add)
buttonclear=Button(root,text="clear",padx=30,pady=15,command=clear)
buttonsubtract= Button(root,text="-",padx=30,pady=15,command=subtract)
buttondivide= Button(root,text="/",padx=30,pady=15,command=divide)
buttonmultiply= Button(root,text="x",padx=30,pady=15,command=times)




button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button_equal.grid(row=4,column=1)
buttonclear.grid(row=4,column=0)
buttonadd.grid(row=4,column=2)
buttonmultiply.grid(row=5,column=2)
buttondivide.grid(row=5,column=1)
buttonsubtract.grid(row=5,column=0)








root.mainloop()
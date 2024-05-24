from tkinter import *


screen=Tk()
screen.geometry("720x480")
screen.title("GUI")


Age=IntVar()
full_name=StringVar()
def Dispaly():
    Label(screen,text="Age:",fg="black",font=14,).grid(row=2,column=1)
    Label(screen,text="Full name:",fg="black",font=14,).grid(row=3,column=1)
    Entry(screen,font=12,textvariable=Age,width=20,borderwidth=5).grid(row=2,column=2)
    Entry(screen,font=12,textvariable=full_name,width=20,borderwidth=5).grid(row=3,column=2)
    
    display=Label(screen,fg="blue", bg="silver",width=40,height=5)
    display.grid(row=6,column=2)
    


    def Result():
        name=full_name.get()
        age=Age.get()
        display.config(text="my age is :: "+str(age)+"name is ::"+str(name))
        print("my name is ",name,"i am ",age)
    
    Button(screen,text="result",fg="red",bg="blue",width=15,borderwidth=5,command=Result).grid(row=4,column=2)


Button(screen,text="Display",fg="blue",font=14,width=15,bg="red",command=Dispaly).grid(row=1,column=2)




screen.mainloop()
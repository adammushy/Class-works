from tkinter import *

screen=Tk()

screen.geometry("640x480")
screen.title("Beng20 Students")

Label(screen,text="1.Dan Thom",fg="blue",font=14).place(x=0,y=0)
Label(screen,text="2.Beatrice stephen",fg="purple",font=14).place(x=0,y=20)
Label(screen,text="3.John Haule",fg="red",font=14).place(x=0,y=40)


screen.mainloop()
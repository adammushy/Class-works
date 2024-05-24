from tkinter import *

root = Tk()
root.title("Question 3")
root.geometry("250x250")
root.config(padx=50,pady=50)

Label(root, text="Enter a number: ", fg="black").grid(row=1,column=1)
x = IntVar()
Entry(root, textvariable=x, fg="black", bg="grey").grid(row=1, column=2)


def enable():
    number = x.get()
    print(f"The number entered is {number}")

Button(root, text="OnClick", fg="black", bg="grey", command=enable).grid(row=2,column=2)
root.mainloop()
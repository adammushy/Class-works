from tkinter import *

root = Tk()
root.title("Question 2")
root.geometry("250x250")


def enable():
    Label(root, text="Enter the length: ", fg="black").grid(row=1, column=1)
    length = IntVar()
    Entry(root, textvariable=length, fg="black", bg="grey").grid(row=1,column=2)
    Label(root, text="Enter the width: ", fg="black").grid(row=2,column=1)
    width = IntVar()
    Entry(root, textvariable=width, fg="black", bg="grey").grid(row=2,column=2)

    e_label = Label(root, fg="black").grid(row=3,column=1)

    def area_of_rectangle():
        l = length.get()
        w = width.get()
        area = l*w
        e_label.config(text=f"The area is {area}")
        print(f"The area of rectangle is {area}")
    Button(root, text="display", fg="black", bg="grey", command=area_of_rectangle).grid(row=4,column=2)


Button(root, text="OnClick", fg="black", bg="grey", command=enable).grid(row=0,column=2)
root.mainloop()
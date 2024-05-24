from tkinter import *

root = Tk()
root.title("Question 1")
root.geometry("250x50")
root.config(padx=200,pady=50)

def enable():
    Label(root, text="Enter the first number: ", fg="black").grid(row=1,column=1)
    f_number = IntVar()
    Entry(root, textvariable=f_number, bg="grey", fg="black").grid(row=1,column=2)
    Label(root, text="Enter the second number: ", fg="black").grid(row=2,column=1)
    s_number = IntVar()
    Entry(root, textvariable=s_number, fg="black", bg="grey").grid(row=2,column=2)

    e_label = Label(root, fg="black").grid(row=3,column=1)

    def addition():
        first_number = f_number.get()
        second_number = s_number.get()
        sum = first_number+second_number
        e_label.config(text="The sum is "+str(sum))
    Button(root, text="Add", fg="black", bg="grey", command=addition).grid(row=4, column=2)


Button(root, text="OnClick", command=enable, fg="black", bg="grey").grid(row=0,column=2)
root.mainloop()

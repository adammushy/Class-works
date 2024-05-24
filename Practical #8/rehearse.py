from tkinter import *

root = Tk()
root.geometry("250x50")
root.config(padx=200, pady=50)

def enable():
    Label(root, text="Enter the first number: ", font=12, fg="black").grid(row=1,column=1)
    x = IntVar()
    Entry(root, textvariable=x, fg="black", font=12, bg="grey").grid(row=1,column=2)
    Label(root, text="Enter the second number: ", font=12, fg="black").grid(row=2, column=1)
    y = IntVar()
    Entry(root, textvariable=y, fg="black", font=12, bg="grey").grid(row=2, column=2)

    e_label = Label(root, fg="black").grid(row=3,column=2)

    def addition():
        first_number = x.get()
        second_number = y.get()
        sum = first_number+second_number
        print(f"The sum is {sum}")
        e_label.config(text=f"The sum is {sum}")
    Button(root, text="AddNumbers", fg="black", bg="grey", command=addition).grid(row=4, column=2)


Button(root, text="OnClick", fg="black", bg="grey", command=enable).grid(row=0,column=2)
root.mainloop()
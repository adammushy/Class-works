from tkinter import *
import tkinter.messagebox


root = Tk()
root.geometry("650x400+300+300")

root.title("Simple Calculator")

switch = None


def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)


def btnp_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')


def btnc_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')


def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


def btneq_clicked(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

    except:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")



data = StringVar()

disp = Entry(root, font="Verdana 20", fg="black", bg="grey", bd=0, justify=RIGHT, insertbackground="#abbab1", cursor="arrow")
disp.bind("<Escape>", btnc_clicked)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)

# Row 1 Buttons
btnrow1 = Frame(root)
btnrow1.pack(expand=TRUE, fill=BOTH)


btn9 = Button(btnrow1, text="9", font="Segoe 23", relief=GROOVE, bd=0, command=btn9_clicked, fg="white", bg="#333333")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow1, text="8", font="Segoe 23", relief=GROOVE, bd=0, command=btn8_clicked, fg="white", bg="#333333")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn7 = Button(btnrow1, text="7", font="Segoe 23", relief=GROOVE, bd=0, command=btn7_clicked, fg="white", bg="#333333")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Row 2 Buttons

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)


btn6 = Button(btnrow2, text="6", font="Segoe 23", relief=GROOVE, bd=0, command=btn6_clicked, fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow2, text="5", font="Segoe 23", relief=GROOVE, bd=0, command=btn5_clicked, fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)


btn4 = Button(btnrow2, text="4", font="Segoe 23", relief=GROOVE, bd=0, command=btn4_clicked, fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Row 3 Buttons

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

btn3 = Button(btnrow3, text="3", font="Segoe 23", relief=GROOVE, bd=0, command=btn3_clicked, fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)


btn2 = Button(btnrow3, text="2", font="Segoe 23", relief=GROOVE, bd=0,  command=btn2_clicked, fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn1 = Button(btnrow3, text="1", font="Segoe 23", relief=GROOVE, bd=0, command=btn1_clicked, fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Row 4 Buttons
btnrow4 = Frame(root, bg="#000000")
btnrow4.pack(expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Segoe 23", relief=GROOVE, bd=0, command=btn0_clicked, fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="Clear", font="Segoe 20", relief=GROOVE, bd=0, command=del_clicked, fg="white", bg="#333333")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Row 5 Buttons
btnrow5 = Frame(root, bg="#000000")
btnrow5.pack(expand=TRUE, fill=BOTH)

btnp = Button(btnrow5, text="+", font="Segoe 23", relief=GROOVE, bd=0, command=btnp_clicked, fg="white", bg="#333333")
btnp.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow5, text="=", font="Segoe 23", relief=GROOVE, bd=0, command=btneq_clicked, fg="white", bg="#333333")
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)


root.mainloop()
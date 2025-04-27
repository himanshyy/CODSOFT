from tkinter import *
import random, string

root = Tk()
root.geometry("400x280")
root.title("Password Generator")


title = StringVar()
Label(root, textvariable=title).pack()
title.set("The strength of password:")

def selection():
    selection = choice.get()

choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root, text="ADVANCED", variable=choice, value=3, command=selection).pack(anchor=CENTER)

labelchoice = Label(root)
labelchoice.pack()


lenlabel = StringVar()
lenlabel.set("Password Length")
Label(root, textvariable=lenlabel).pack()

val = IntVar()
spinlength = Spinbox(root, from_=8, to=24, textvariable=val, width=13) 
spinlength.pack()


poor = string.ascii_lowercase + string.digits
average = string.ascii_letters + string.digits
symbols = "~!@#$%^&*()_+{}[]\\|:;\"<>,.?/"
advance = average + symbols


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))


def callback():
    lsum.config(text=passgen())

passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3)
passgenButton.pack()


lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

root.mainloop()

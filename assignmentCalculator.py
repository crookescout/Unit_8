# Scout Crooke, 11/19/19, this program is a calculator

from tkinter import *

root = Tk()


def add_zero():
    new_result = display_result.get()
    new_result += "0"
    display_result.set(new_result)


def add_one():
    new_result = display_result.get()
    new_result += "1"
    display_result.set(new_result)


def add_two():
    new_result = display_result.get()
    new_result += "2"
    display_result.set(new_result)


def add_three():
    new_result = display_result.get()
    new_result += "3"
    display_result.set(new_result)


def add_four():
    new_result = display_result.get()
    new_result += "4"
    display_result.set(new_result)


def add_five():
    new_result = display_result.get()
    new_result += "5"
    display_result.set(new_result)


def add_six():
    new_result = display_result.get()
    new_result += "6"
    display_result.set(new_result)


def add_seven():
    new_result = display_result.get()
    new_result += "7"
    display_result.set(new_result)


def add_eight():
    new_result = display_result.get()
    new_result += "8"
    display_result.set(new_result)


def add_nine():
    new_result = display_result.get()
    new_result += "9"
    display_result.set(new_result)


def clear():
    new_result = ""
    display_result.set(new_result)


def divide():
    new_result = display_result.get()
    new_result += "/"
    display_result.set(new_result)


def multiply():
    new_result = display_result.get()
    new_result += "*"
    display_result.set(new_result)


def subtract():
    new_result = display_result.get()
    new_result += "-"
    display_result.set(new_result)


def add():
    new_result = display_result.get()
    new_result += "+"
    display_result.set(new_result)


def equal():
    new_result = display_result.get()
    new_result = eval(new_result)
    display_result.set(new_result)


def percent():
    new_result = display_result.get()
    new_result = float(new_result) / 100
    display_result.set(new_result)


def dot():
    new_result = display_result.get()
    new_result += "."
    display_result.set(new_result)


def plus_minus():
    new_result = display_result.get()
    new_result = float(new_result) * -1
    display_result.set(new_result)


display_result = StringVar()
display = Entry(root, textvariable=display_result, justify="right")
display.grid(row=2, column=1, columnspan=4)


title = Label(root, text="Calculator", font="Helvetica 20")
title.grid(row=1, column=1, columnspan=4)

clear_button = Button(root, text="Clear", width=4, font="Helvetica 16", command=clear)
clear_button.grid(row=3, column=1)

plus_minus_button = Button(root, text="+/-", width=4, font="Helvetica 16", command=plus_minus)
plus_minus_button.grid(row=3, column=2)

percent_button = Button(root, text="%", width=4, font="Helvetica 16", command=percent)
percent_button.grid(row=3, column=3)

divide_button = Button(root, text="/", width=4, font="Helvetica 16", command=divide)
divide_button.grid(row=3, column=4)

seven_button = Button(root, text="7", width=4, font="Helvetica 16", command=add_seven)
seven_button.grid(row=4, column=1)

eight_button = Button(root, text="8", width=4, font="Helvetica 16", command=add_eight)
eight_button.grid(row=4, column=2)

nine_button = Button(root, text="9", width=4, font="Helvetica 16", command=add_nine)
nine_button.grid(row=4, column=3)

multiply_button = Button(root, text="*", width=4, font="Helvetica 18", command=multiply)
multiply_button.grid(row=4, column=4)

four_button = Button(root, text="4", width=4, font="Helvetica 16", command=add_four)
four_button.grid(row=5, column=1)

five_button = Button(root, text="5", width=4, font="Helvetica 16", command=add_five)
five_button.grid(row=5, column=2)

six_button = Button(root, text="6", width=4, font="Helvetica 16", command=add_six)
six_button.grid(row=5, column=3)

minus_button = Button(root, text="-", width=4, font="Helvetica 16", command=subtract)
minus_button.grid(row=5, column=4)

one_button = Button(root, text="1", width=4, font="Helvetica 16", command=add_one)
one_button.grid(row=6, column=1)

two_button = Button(root, text="2", width=4, font="Helvetica 16", command=add_two)
two_button.grid(row=6, column=2)

three_button = Button(root, text="3", width=4, font="Helvetica 16", command=add_three)
three_button.grid(row=6, column=3)

plus_button = Button(root, text="+", width=4, font="Helvetica 16", command=add)
plus_button.grid(row=6, column=4)


zero_button = Button(root, text="0", width=4, font="Helvetica 16", command=add_zero)
zero_button.grid(row=7, column=1)

dot_button = Button(root, text=".", width=4, font="Helvetica 16", command=dot)
dot_button.grid(row=7, column=2)

equal_button = Button(root, text="=", width=9, font="Helvetica 16", command=equal)
equal_button.grid(row=7, column=3, columnspan=2)


root.mainloop()

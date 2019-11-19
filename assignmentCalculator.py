# Scout Crooke, 11/19/19, this program is a calculator

from tkinter import *

root = Tk()

title = Label(root, text="Calculator", font="Helvetica 24")
title.grid(row=1, column=1, columnspan=4)

result_bar = Entry(root)
result_bar.grid(row=2, column=1, columnspan=4)

clear_button = Button(root, text="Clear", width=4, font="Helvetica 18")
clear_button.grid(row=3, column=1)

plus_minus_button = Button(root, text="+/-", width=4, font="Helvetica 18")
plus_minus_button.grid(row=3, column=2)

percent_button = Button(root, text="%", width=4, font="Helvetica 18")
percent_button.grid(row=3, column=3)

divide_button = Button(root, text="/", width=4, font="Helvetica 18")
divide_button.grid(row=3, column=4, sticky="E")

seven_button = Button(root, text="7", width=4, font="Helvetica 18")
seven_button.grid(row=4, column=1)

eight_button = Button(root, text="8", width=4, font="Helvetica 18")
eight_button.grid(row=4, column=2)

nine_button = Button(root, text="9", width=4, font="Helvetica 18")
nine_button.grid(row=4, column=3)

multiply_button = Button(root, text="*", width=4, font="Helvetica 18")
multiply_button.grid(row=4, column=4)


four_button = Button(root, text="4", width=4, font="Helvetica 18")
four_button.grid(row=5, column=1)

five_button = Button(root, text="5", width=4, font="Helvetica 18")
five_button.grid(row=5, column=2)

six_button = Button(root, text="6", width=4, font="Helvetica 18")
six_button.grid(row=5, column=3)

minus_button = Button(root, text="-", width=4, font="Helvetica 18")
minus_button.grid(row=5, column=4)

root.mainloop()

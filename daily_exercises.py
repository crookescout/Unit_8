# Scout Crooke, 11/15/19, this function works on daily exerceises for Unit 8

from tkinter import *

root = Tk()

# 1
#
# hello_label = Label(root, text="Hello, World")
# hello_label.grid(row=1, column=1)

# 2

#
# def say_hello():
#     other_name = user_name.get()
#     if other_name == "":
#         name.set("You forgot to enter your name")
#     else:
#         name.set("Hello, " + other_name)
#
#
# user_name = StringVar()
# name = StringVar()
# enter_name = Entry(root, textvariable=user_name)
# enter_name.grid(row=1, column=1)
#
# hello_label = Label(root, textvariable=name)
# hello_label.grid(row=2, column=1)
#
# hello_button = Button(root, text="Say Hello", command=say_hello)
# hello_button.grid(row=3, column=1)

# 3


def convert_temp():
    new_temp = (temp - 32) * 5/9
    return new_temp


temp = IntVar()
new_temp = IntVar()
enter_temp = Entry(root, text="degrees F:", textvariable=temp)
enter_temp.grid(row=1, column=2)

degreeF_label = Label(root, text="degrees F:")
degreeF_label.grid(row=1, column=1)

degreeC_label = Label(root, text="degrees C:")
degreeC_label.grid(row=2, column=1)

convert_button = Button(root, text="Convert", command=convert_temp)
convert_button.grid(row=3, column=2)


root.mainloop()

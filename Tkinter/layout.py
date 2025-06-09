from tkinter import *

# Pack will start from top and pack every other widget below the prev one.
# Place is all about pre-sized positioning.
# Any widget created in the screen must be packed, placed or grid in order to be shown.
# You can not mix pack & grid in the same program!

window = Tk()  # Create the main window.
window.title("My GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = Label(text="The Label", font=("Arial", 24))
my_label.config(text="New Text")
# my_label.pack()  # Place/layout it into the screen and center it.
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

button = Button(text="Click Me")
button.grid(column=1, row=1)

button = Button(text="New Button")
button.grid(column=2, row=0)

entry = Entry(width=10)
entry.grid(column=3, row=2)

window.mainloop()
#
#
# def button_clicked():
#     my_label.config(text=entry.get())
#
#
# button = Button(text="Click Me", command=button_clicked)
# button.pack()
#
# entry = Entry(width=10)
# entry.insert(END, "Enter the text")
# entry.pack()
#
# window.mainloop()  # Keep the window on screen.

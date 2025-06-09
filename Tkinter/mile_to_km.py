from tkinter import *


# Pack will start from top and pack every other widget below the prev one.
# Place is all about pre-sized positioning.
# Any widget created in the screen must be packed, placed or grid in order to be shown.
# You can not mix pack & grid in the same program!

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")


window = Tk()  # Create the main window.
window.title("Miles to Km Converter")
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()

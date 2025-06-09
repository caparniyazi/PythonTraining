from tkinter import *

window = Tk()  # Create the main window.
window.title("My GUI")
window.minsize(width=500, height=300)

my_label = Label(text="The Label", font=("Arial", 24))
my_label.pack()  # Place/layout it into the screen and center it.
my_label["text"] = "New Text"
my_label.config(text="New Text..")


def button_clicked():
    my_label.config(text=entry.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

entry = Entry(width=10)
entry.insert(END, "Enter the text")
entry.pack()

text_area = Text(height=5, width=30)
text_area.focus()
text_area.insert(END, "Example of multiline text")
# Get the current value in textbox at line1, character 0
print(text_area.get("1.0", END))
text_area.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


def scale_used(value):
    print(value)


def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option1", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


def listbox_used(event):
    # Get the current selection from the listbox.
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()  # Keep the window on screen.

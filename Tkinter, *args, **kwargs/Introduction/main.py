from tkinter import *
window = Tk()
window.title("GUI Program")
window.minsize(500,300)

# LABEL

label = Label(text="Label", font=("Arial", 24, "bold"))
label.pack()
# label.config(text="New Text")


# BUTTON
def button_click():
    label["text"] = input.get()


button = Button(text="Click Me", command=button_click)
button.pack()


# ENTRY

input = Entry(width=10)
input.pack()

window.mainloop()

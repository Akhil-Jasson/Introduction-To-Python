from tkinter import *

window = Tk()
window.minsize(500,200)
window.title("Mile to Km Converter")
window.config(padx=150, pady=50)

input = Entry(width=15)
input.insert(END, string="0")
input.grid(row=0, column=1)

miles = Label(text="Miles", padx=10)
miles.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

value = Label(text=0)
value.grid(row=1, column=1)

km = Label(text="Km")
km.grid(row=1, column=2)


def calculate_clicked():
    value["text"] = int(input.get())*1.609


calculate = Button(text="Calculate", command=calculate_clicked)
calculate.grid(row=2, column=1)

window.mainloop()

from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=240, height=240)
PwLogo = PhotoImage(file="logo.png")
canvas.create_image(120, 120, image=PwLogo)
canvas.pack()




window.mainloop()

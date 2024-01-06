from tkinter import *
from tkinter import messagebox
import random
import pyperclip  # Used for copying text to the clipboard
# ---------------------------- PASSWORD GENERATOR -------------------------------
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for j in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for k in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    # passName = ""
    # for char in password_list:
    #   passName += char

    entry3.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button():
    websiteName = entry1.get()
    emailName = entry2.get()
    passName = entry3.get()
    if len(websiteName) == 0 or len(passName) == 0:
        messagebox.showinfo(title="Oops!", message="Make sure all the fields are filled")
    else:
        is_ok = messagebox.askokcancel(title=websiteName, message=f"These are the details entered: \nEmail: {emailName}\nPassword: {passName}")
        if is_ok:
            data = open("data.txt", "a")
            data.write(f"{websiteName}|{emailName}|{passName}")
            data.write("\n")
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
PwLogo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=PwLogo)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

GenPass = Button(width=14, text="Generate Password", command=gen_pass)
GenPass.grid(row=3, column=2)


add = Button(width=36, text="Add", command=add_button)
add.grid(row=4, column=1, columnspan=2)

entry1 = Entry(width=35)
entry1.grid(row=1, column=1, columnspan=2)
entry1.focus()

entry2 = Entry(width=35)
entry2.grid(row=2, column=1, columnspan=2)
entry2.insert(0,"akhilinian@gmail.com")


entry3 = Entry(width=22)
entry3.grid(row=3, column=1)


window.mainloop()

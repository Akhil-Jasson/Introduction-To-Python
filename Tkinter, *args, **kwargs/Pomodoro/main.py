from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100,background="purple")

canvas = Canvas(width=224, height=224, highlightthickness=0)
pomo_img = PhotoImage(file="pomodoro.png")
canvas.create_image(112,112,image=pomo_img)
canvas.create_text(112, 112, text="00:00", fill="purple", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Timer", font=("calibri", 22, "bold"), background="purple",fg="yellow")
timer.grid(row=0, column=1)

start = Button(text="Start")
start.grid(row=2, column=0)

reset = Button(text="Reset")
reset.grid(row=2, column=2)

check = Label(text="✔",fg="green", background="purple", font= ("calibri",25, "bold"))
check.grid(row=4, column=1)


window.mainloop()

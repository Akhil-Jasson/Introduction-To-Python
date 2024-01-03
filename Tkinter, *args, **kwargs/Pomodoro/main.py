from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = -1
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = -1
    check["text"] = ""
    start_count()
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_count():
    global reps
    reps += 1
    if reps % 2 == 0 and reps < 8:
        count_down(WORK_MIN * 60)
        timer.config(text="Work", fg="red")
        if reps != 0:
            check["text"] += "✔"
    elif reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer.config(text="Long Break", fg="green")
    elif reps == 9:
        check["text"] += "✔"
    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text="Short Break", fg="pink")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
    elif count == 0:
        start_count()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, background="purple")

canvas = Canvas(width=224, height=224, highlightthickness=0)
pomo_img = PhotoImage(file="pomodoro.png")
canvas.create_image(112, 112, image=pomo_img)
timer_text = canvas.create_text(112, 112, text="00:00", fill="purple", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Timer", font=("calibri", 22, "bold"), background="purple", fg="yellow")
timer.grid(row=0, column=1)

start = Button(text="Start", command=start_count)
start.grid(row=2, column=0)

reset = Button(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

check = Label(fg="yellow", background="purple", font=("calibri", 25, "bold"))
check.grid(row=4, column=1)


window.mainloop()

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    display['text'] = 'Timer'
    display['fg'] = YELLOW
    display['font'] = (FONT_NAME,40,"bold")
    tick['text'] = ""
    canvas.itemconfig(timer_text,text = "00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps = reps + 1
    if reps % 8 == 0:
        display['text'] = "Long Break"
        display['fg'] = RED
        countdown(LONG_BREAK_MIN * 60)

    elif reps % 2 == 0:
        display['text'] = "Short Break"
        display['fg'] = PINK
        countdown(SHORT_BREAK_MIN * 60)
    else:
        display['text'] = "Work Time"
        display['fg'] = "yellow"
        countdown(WORK_MIN * 60)
        tick['text'] += "✔"






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    sec = count % 60
    if int(sec / 10) == 0:
        sec = f"0{sec}"

    minute = int(count / 60)
    if int(minute / 10) == 0:
        minute = f"0{minute}"
    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    print(count)
    if count > 0 and reps > 0:
        timer = window.after(1000, countdown,count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
temp = Label(window, text="", bg=GREEN)
temp.grid(row=0, column=0)
display = Label(window, text="Timer", bg=GREEN, fg=YELLOW, font=(FONT_NAME, 40, "bold"))
display.grid(row=0, column=1)
tick = Label(window, text="", fg=PINK, bg=GREEN, font=(FONT_NAME, 15, "bold"))
tick.grid(row=2, column=1)

window.config(padx=100, pady=50, bg=GREEN)
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
res = Button(window, text='Reset', bg=RED, fg=YELLOW, font=(FONT_NAME, 15, "bold"),command = reset_timer)
res.grid(row=2, column=2)
strt = Button(window, text='Start', bg=RED, fg=YELLOW, font=(FONT_NAME, 15, "bold"), command=start_timer)
strt.grid(row=2, column=0)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
window.mainloop()

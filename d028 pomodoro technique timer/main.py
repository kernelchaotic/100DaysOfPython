from tkinter import *
import tkinter.messagebox
import math

# ---------------------------- CONSTANTS AND GLOBALS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
BUTTON_FONT = ("Arial", 12, "bold")
CHECKMARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 8
timer = None
checkmark_tracker = ""


# ---------------------------- POP-UP BOXES ------------------------------- #

def popup(title, text):
    tkinter.messagebox.showinfo(title=title, message=text)


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps, checkmark_tracker
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    reps = 8
    checkmark_tracker = ""
    pomodoro_tracker_check.config(text=checkmark_tracker)
    popup(title="Timer Reset", text="The timer has been reset.")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    working_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        timer_label.config(text="Work", fg=GREEN)
        working_countdown(working_sec)
        reps -= 1
    elif reps == 1:
        timer_label.config(text="Break", fg=RED)
        working_countdown(long_break_sec)
        reps = 8
    elif reps % 2 == 1:
        timer_label.config(text="Break", fg=PINK)
        working_countdown(short_break_sec)
        reps -= 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def working_countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, working_countdown, count - 1)
    else:
        window.lift()
        global reps, checkmark_tracker
        if reps == 8:
            popup(title="Break over!", text="Time to get back to work! Click \"start\" to begin.")
            checkmark_tracker = ""
            pomodoro_tracker_check.config(text=checkmark_tracker)
        elif reps % 2 == 1:
            checkmark_tracker += CHECKMARK
            pomodoro_tracker_check.config(text=checkmark_tracker)
            if reps == 1:
                popup(title="Work time completed!", text="Time for a 20 minute break! Click \"start\" to begin!")
            else:
                popup(title="Work time completed!", text="Time for a 5 minute break! Click \"start\" to begin.")
        elif reps % 2 == 0:
            popup(title="Break over!", text="Time to get back to work! Click \"start\" to begin.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# labels
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

pomodoro_tracker_check = Label(font=("Arial", 15), fg=GREEN, bg=YELLOW)
pomodoro_tracker_check.grid(column=1, row=3)

# buttons
start_button = Button(text="Start", font=BUTTON_FONT, fg="white", bg=GREEN, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=BUTTON_FONT, fg="white", bg=GREEN, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# canvas with tomato and timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 138, text="00:00", font=(FONT_NAME, 25, 'bold'), fill="white")
canvas.grid(column=1, row=1)


window.mainloop()

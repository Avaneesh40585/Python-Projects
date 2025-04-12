from tkinter import *
# *---------------------------- CONSTANTS -------------------------------* #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BROWN = "#964B00"
# colors extracted from: https://colorhunt.co/

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# *---------------------------- TIMER RESET -------------------------------* # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="Click Start",font=(FONT_NAME,25,"bold"))
    timer_label.config(text="Mode",fg=BROWN)
    global reps
    reps=0
    counter_label.config(text=f"#{reps}")
# *---------------------------- TIMER MECHANISM -------------------------------* # 
def start_timer():
    global reps
    reps+=1
    counter_label.config(text=f"#{(reps-1)//2 +1}")
    if(reps%8==0):
        timer_label.config(text="Break",fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif(reps%2==0):
        timer_label.config(text="Break",fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        timer_label.config(text="Work",fg=GREEN)
        count_down(WORK_MIN*60)
# *---------------------------- COUNTDOWN MECHANISM -------------------------------* # 
def count_down(count):
    display_min=count//60
    display_sec=count%60
    if display_sec<10:
        display_sec=f"0{display_sec}"
    canvas.itemconfig(timer_text, text=f"{display_min}:{display_sec}",font=(FONT_NAME,35,"bold"))
    if count>=0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
# *---------------------------- UI SETUP -------------------------------* #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

# Canvas:
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_png=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_png)
timer_text=canvas.create_text(100,130, text="Click Start",fill="white",font=(FONT_NAME,25,"bold"))
canvas.grid(row=1,column=1)

# Labels:
timer_label=Label(bg=YELLOW,fg=BROWN,text="Mode",font=(FONT_NAME,50))
timer_label.grid(row=0,column=1)
counter_label=Label(bg=YELLOW,fg=GREEN,text=f"#{reps}",font=(FONT_NAME,20))
counter_label.grid(row=3,column=1)

# Buttons:
start_button=Button(text="Start",highlightbackground=YELLOW,command=start_timer)
start_button.grid(row=2,column=0)
reset_button=Button(text="Reset",highlightbackground=YELLOW,command=reset_timer)
reset_button.grid(row=2,column=2)

window.mainloop()

from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
# *----------------------- DATA MANAGEMENT --------------------------* #
try:
    df=pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df=pandas.read_csv("./data/french_words.csv")
to_learn=df.to_dict(orient="records")
current_card={}
# *----------------------- EVALUATION FUNCTIONS ----------------------* #
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title, text='French',fill="black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(card_image,image=card_front_png)
    flip_timer=window.after(3000,func=flip_card)
    
def flip_card():
    global current_card
    canvas.itemconfig(card_image,image=card_back_png)
    canvas.itemconfig(card_title,text='English',fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")

def known_word():
    to_learn.remove(current_card)
    new_df=pandas.DataFrame(to_learn)
    new_df.to_csv("./data/words_to_learn.csv",index=False)
    next_card()
# *---------------------------- UI SETUP -----------------------------* #
window=Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

# Canvas:
canvas=Canvas(width=800,height=526)
card_front_png=PhotoImage(file="./images/card_front.png")
card_back_png=PhotoImage(file="./images/card_back.png")
card_image=canvas.create_image(400,263,image=card_front_png)
card_title=canvas.create_text(400,150,text="Title",fill="black",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="Word",fill="black",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


# Buttons:
wrong_button_png=PhotoImage(file="./images/wrong.png")
wrong_button=Button(image=wrong_button_png,command=next_card)
wrong_button.config(highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1,column=0)

right_button_png=PhotoImage(file="./images/right.png")
right_button=Button(image=right_button_png,command=known_word)
right_button.config(highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=1,column=1)

next_card()

window.mainloop()

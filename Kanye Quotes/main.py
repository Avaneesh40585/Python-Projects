from tkinter import *
import requests
# *---------------------------- DATA MANAGEMENT -----------------------------------* #
FONT_SIZES=[(150,15), (120,18), (90,21), (70,24), (50,27), (30,30), (20,33), (12,36), (1,39)]
def fit_fontsize( n_chars):
    for (chars, font_size) in FONT_SIZES:
        if n_chars > chars:
            return font_size
 
def get_quote():
    response = requests.get('https://api.kanye.rest/')
    response.raise_for_status()
    quote = response.json()['quote']
    font_size = fit_fontsize( len( quote))
    canvas.itemconfigure( quote_text, text=response.json()['quote'], font=("Arial", font_size, 'bold'))
# *--------------------------------- UI SETUP --------------------------------------* #
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Tap on me", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, highlightbackground="black")
kanye_button.grid(row=1, column=0)

window.mainloop()
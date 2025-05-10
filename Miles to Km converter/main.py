from tkinter import *

window=Tk()
window.title("Miles to km converter")
window.minsize(width=400,height=200)
window.configure(padx=50,pady=50)

def button_click():
    miles=float(input.get())
    km=1.609*miles
    km_value_label["text"]=str(km)
    
# Entry:
input=Entry(width=5)
input.grid(row=0,column=1)

# Labels:
miles_label=Label(text="miles",font=("Comfortaa",24,"bold"))
miles_label.grid(row=0,column=2)

is_equal_to_label=Label(text="is equal to",font=("Comfortaa",24,"bold"))
is_equal_to_label.grid(row=1,column=0)

km_value_label=Label(text="0",font=("Comfortaa",24,"bold"))
km_value_label.grid(row=1,column=1)

km_label=Label(text="km",font=("Comfortaa",24,"bold"))
km_label.grid(row=1,column=2)

# Button:
button=Button(text="Convert",command=button_click)
button.grid(row=2,column=1)

window.mainloop()

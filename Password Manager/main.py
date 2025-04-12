from tkinter import *
from tkinter import messagebox
from random import choice,shuffle,randint
import pyperclip
import json
# *---------------------------- PASSWORD GENERATOR -------------------------------* #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password_list)
    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    
    # Default way of creating string:
    # password = ""
    # for char in password_list:
    #   password += char
# *---------------------------- SAVE PASSWORD -------------------------------* #
def add_password():
    website_input=website_entry.get()
    username_input=username_entry.get()
    password_input=password_entry.get()
    new_data={
        website_input: {
            "Email/Username": username_input,
            "Password": password_input,
        }
    }
    if website_input=="" or username_input=="" or password_input=="":
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        confirmation_message=f"""Confirm your details entered:
        Website: {website_input}
        Email/Username: {username_input}
        Password: {password_input}"""
        confirmation=messagebox.askokcancel(title="Confirm your details!",message=confirmation_message)
        if confirmation:
            # * Json file data management:
            try:
                with open(file="password_data.json",mode="r") as data_file:
                    data=json.load(data_file)
            except FileNotFoundError :
                with open(file="password_data.json",mode="w") as data_file:
                    json.dump(new_data,data_file, indent=4)
            else:
                data.update(new_data)
                with open(file="password_data.json",mode="w") as data_file:
                    json.dump(data,data_file, indent=4)
            finally:
                website_entry.delete(0,END)
                username_entry.delete(0,END)
                password_entry.delete(0,END)
            
            # * Default way of file data management:
            # with open(file="password_data.txt",mode='a') as data:
            #     data.write("--------------------------------------------------------------\n")
            #     data.write(f"Website: {website_input}\n")
            #     data.write(f"Email/Username: {username_input}\n")
            #     data.write(f"Password: {password_input}\n")

# *---------------------------- FIND PASSWORD -------------------------------* #
def search_password():
    website_input=website_entry.get()
    try:
        with open(file="password_data.json",mode="r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(mesage="No Data file found.")
    else:
        found=False
        for key in data.keys():
            if(website_input.title()==key.title()):
                messagebox.showinfo(message=f"Website: {key}\nEmail/Username: {data[key]["Email/Username"]}\nPassword: {data[key]["Password"]}")
                found=True
                break
        if(not found):
            messagebox.showinfo(message=f"No details exists for the entered {website_input} website, Try checking for any possible spelling errors.")
    
# *---------------------------- UI SETUP -------------------------------* #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


# Canvas:
canvas=Canvas(height=200,width=200)
logo_png=PhotoImage(file="logo.png")
canvas.create_image(105,100, image=logo_png)
canvas.grid(row=0,column=1)


# Labels:
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

username_label=Label(text="Email/Username:")
username_label.grid(row=2,column=0)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)


# Entries:
website_entry=Entry(width=20)
website_entry.focus()
website_entry.grid(row=1,column=1)

username_entry=Entry(width=35)
# username_entry.insert(0, "Example@email.com")
username_entry.grid(row=2,column=1,columnspan=2)

password_entry=Entry(width=20)
password_entry.grid(row=3,column=1)


# Buttons:
generate_button=Button(text="Generate Password",width=11,command=generate_password)
generate_button.grid(row=3,column=2)

add_button=Button(text="Add",width=33,command=add_password)
add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(text="Search",width=11,command=search_password)
search_button.grid(row=1,column=2)

window.mainloop()
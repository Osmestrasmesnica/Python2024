from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

BLUE = "#4C4C6D"
GREEN = "#1B9C85"
WHITE = "#e8f6ef"
YELLOW = "#FFE194"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("Dan_30_Errors_Exceptions_JSON/password_manager/data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("Dan_30_Errors_Exceptions_JSON/password_manager/data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("Dan_30_Errors_Exceptions_JSON/password_manager/data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ------------------------- SEARCH ACCOUNT ---------------------------- #
                
def find_password():
    website = website_entry.get().title()
    try:
        with open("Dan_30_Errors_Exceptions_JSON/password_manager/data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message=f"Spisak sifra je trenutno prazan. Ubacite prvu sifru u fajl.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"Nisu pronadjeni podaci za {website}.")
    finally:
        website_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="Dan_30_Errors_Exceptions_JSON/password_manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:", font=(FONT_NAME, 12) , fg= GREEN, background=WHITE)
website_label.grid(row=1, column=0, sticky=E)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 12) , fg= GREEN, background=WHITE)
email_label.grid(row=2, column=0, sticky=E)

password_label = Label(text="Password:", font=(FONT_NAME, 12) , fg= GREEN, background=WHITE)
password_label.grid(row=3, column=0, sticky=E)

#Entries
website_entry = Entry(width=22)
website_entry.grid(row=1, column=1, sticky=EW)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
email_entry.insert(0, "wlq.aleksa@gmail.com")

password_entry = Entry(width=22, textvariable="", show="*")
password_entry.grid(row=3, column=1, sticky=EW)

# Buttons
generate_password_button = Button(text="Generate Password", width=16, command=generate_password, highlightthickness=0, background=YELLOW, fg=GREEN)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save, highlightthickness=0, background=YELLOW, fg=GREEN)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

#TODO Dodati command= find_password
search_button = Button(text="Search", command=find_password, width=16, highlightthickness=0, background=YELLOW, fg=GREEN,)
search_button.grid(row=1, column=2, sticky=EW)

window.mainloop()
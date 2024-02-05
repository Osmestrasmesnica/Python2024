#! PYTHON DAN 29
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

BLUE = "#4C4C6D"
GREEN = "#1B9C85"
WHITE = "#e8f6ef"
YELLOW = "#FFE194"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Generate strong password with letters, symbols and numbers."""
    
    #*Password Generator Project - Dan_05
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Random se bira u range koji smo zadali po slovo, simbol i broj i spajamo u password_list
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    # Pravimo da budu random karakteri u sifri
    shuffle(password_list)
    # Spajamo u jedan string
    password = "".join(password_list)
    # Ubacujemo u input odmah generisan password
    input_password.insert(0, password) # --> 0 je odakle se pocinje, sledece je sta se unosi

    pyperclip.copy(password)

    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    """Save data to data.txt file and clear inputs"""

    website = input_website.get()
    username = input_username.get()
    password =  input_password.get()

    # validation
    if len(username) == 0 or len(password) == 0 or len(website) == 0:
        # messagebox.showerror(title="Error", message="Popunite sva polja!")
        messagebox.showwarning(title="Error", message="Popunite sva polja!")
    else:
        # messagebox.showinfo(title="Title", message="message")
        is_ok = messagebox.askokcancel(title="Password Menager Confirmation", message=f"Uneli ste:\nSajt: {website}:\nUsername: {username}\nPassword: {password}\nDa li želite da sačuvate ove podatke?")

        if is_ok:
            with open("c:/Aleksa Vlku/Dokumenta/DROWSSAP/data.txt", "a") as f:
                f.write(input_website.get() + " | " + input_username.get() + " | " + input_password.get() + "\n")
            print(f"Sajt {input_website.get()} dodat je u data.txt.")
            input_website.delete(0, END)
            input_username.delete(0, END)
            input_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
    
window = Tk()
window.title("Password Manager by WLQ")
window.config(padx=50, pady=50, background= WHITE)

#! CANVAS
canvas = Canvas(width=200, height=200, highlightthickness= 0, background= WHITE)
password_img = PhotoImage(file="Dan_29_Password_manager_APP/logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

#! LABEL
label_website = Label(text= "Website:", font=(FONT_NAME, 12) , fg= GREEN, background=WHITE)
label_website.grid(row=1, column=0, sticky=E) #! --> Sticky Labels to the right
label_username = Label(text= "Email/Username:", font=(FONT_NAME, 12) , fg= GREEN, background=WHITE)
label_username.grid(row=2, column=0, sticky=E)
label_password = Label(text= "Password:", font=(FONT_NAME, 12) , fg= GREEN, background=WHITE)
label_password.grid(row=3, column=0, sticky=E)

#! INPUTS
input_website = Entry(width=35)
input_website.focus()
input_website.grid(row=1, column=1, columnspan=2, sticky=EW) #! --> East and West edges (ie left and right) will stick to the grid

input_username = Entry(width=35)
input_username.insert(0, "") #! --> Dodati u "" ovde neki email koji ce uvek da ti se automatski popuni
input_username.grid(row=2, column=1, columnspan=2, sticky=EW)

input_password = Entry(width=21, textvariable="", show="*")
input_password.grid(row=3, column=1, sticky=EW)

#! BUTTON
generate_password_btn = Button(text="Generate Password", highlightthickness=0, background=YELLOW, fg=GREEN, command=generate_password)
generate_password_btn.grid(row= 3,column=2)

add_btn = Button(text="Add", width= 36, highlightthickness=0, background=YELLOW, fg=GREEN, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2, sticky=EW)

#! STANDAR DIALOGS (POP UPS)

window.mainloop()
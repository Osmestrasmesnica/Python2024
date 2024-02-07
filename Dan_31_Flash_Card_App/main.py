from tkinter import *
import pandas as pd
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Ariel", 30, "italic")
FONT_WORD = ("Ariel", 40, "bold")
FONT_NAME = "Courier New"
to_learn = {}
current_card = {}
words_that_i_know = []

try:
    # Pri pokretanju prvo se, ako postoji, otvara words_to_learn.csv
    data = pd.read_csv("Dan_31_Flash_Card_App/data/words_to_learn.csv")
except FileNotFoundError:
    # Ako ne postoji, otvara fajl german.csv
    original_data = pd.read_csv("Dan_31_Flash_Card_App/data/german.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



# ----------------------------- METHODS -------------------------------- #

def next_card():
    global flip_timer_eng, flip_timer_srb, current_card

    # ovaj deo koda sprecava da se timer desi iako klikcemo nonstop dugmice
    window.after_cancel(flip_timer_eng)
    window.after_cancel(flip_timer_srb)
    
    # random rec iz dict
    current_card = random.choice(to_learn)
    
    canvas.itemconfig(card_title, text= "German", fill="black")
    canvas.itemconfig(card_word, text= current_card["German"], fill="black")
    canvas.itemconfig(card_bg, image= card_front_bg)

    # Delay nakon koga ce se okrenuti karta sa engleskim pa sa srspkim recima
    flip_timer_eng = window.after(6000, func=flip_card)
    flip_timer_srb = window.after(9000, func=flip_card_srb)


def flip_card():
    canvas.itemconfig(card_title, text= "English", fill= "red")
    canvas.itemconfig(card_word, text= f"{current_card["English"]}", fill= "red" )
    canvas.itemconfig(card_bg, image= card_back_bg)

def flip_card_srb():
    canvas.itemconfig(card_title, text= "Srpski", fill= "yellow")
    canvas.itemconfig(card_word, text= f"{current_card["Srpski"]}", fill= "yellow")
    canvas.itemconfig(card_bg, image= card_back_bg)

def is_known():
    """If i know this word, remove it from the list."""
    
    words_that_i_know.append(current_card)
   


    to_learn.remove(current_card)
    print(len(to_learn))


    next_card()


 
def save_files():
    """ Window close callback function"""
    if messagebox.askyesno("Save Progress", "Do you want to save your progress?") == True:
        # List of dict to DataFrame and then create CSV file
        to_learn_df = pd.DataFrame(to_learn)
        to_learn_df.to_csv("Dan_31_Flash_Card_App/data/words_to_learn.csv", index=False, mode="w")
        # Listo of dict with words that i know
        wrods_learned_df= pd.DataFrame(words_that_i_know)
        wrods_learned_df.to_csv("Dan_31_Flash_Card_App/data/words_i_learned.csv", index=False, mode="a")
        window.destroy()
    else:
        window.destroy()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("NAJČEŠĆE REČI U NEMAČKOM JEZIKU")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer_eng = window.after(3000, func=flip_card)
flip_timer_srb = window.after(6000, func=flip_card_srb)

canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_bg = PhotoImage(file="Dan_31_Flash_Card_App/images/card_front.png")
card_back_bg = PhotoImage(file="Dan_31_Flash_Card_App/images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_bg)
canvas.grid(row=0, column=0, columnspan=2, sticky=EW)

# Naslov jezika i rec na tom jeziku
card_title = canvas.create_text(400, 150, text="", font = FONT_LANGUAGE)
card_word = canvas.create_text(400, 250, text="", font = FONT_WORD)

# ---------------------------- BUTTONS ------------------------------- #

img_right = PhotoImage(file="Dan_31_Flash_Card_App/images/right.png")
btn_right = Button(image=img_right, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground="green", borderwidth=0, command=is_known)
btn_right.grid(row=1, column=1)

img_wrong = PhotoImage(file="Dan_31_Flash_Card_App/images/wrong.png")
btn_wrong = Button(image=img_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground="red", borderwidth=0, command=next_card)
btn_wrong.grid(row=1, column=0)

#generate initial word
next_card()

#set callback for window close
window.protocol("WM_DELETE_WINDOW", save_files)

window.mainloop()

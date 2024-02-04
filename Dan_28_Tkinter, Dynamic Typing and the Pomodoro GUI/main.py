# PYTHON DAN 28
#! Tkinter, Dynamic Typing and the Pomodoro GUI

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None # na pocetku je none a posle jojs e dodeli global

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg = RED)
    label_checkmarks.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_counting():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_brake_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    # Ako je 1/3/5/7 ponavljanje onda se radi 25min, ako je 2/4/6 onda je 5min a ako je 8. onda je 20min
    if REPS % 8 == 0: #! ovo mora prvo da ide pa teko % 2
        count_down(long_break_sec)
        print("Vreme je za dugacku pauzu od 20min")
        label_timer.config(text="Pauza", fg = RED)
    elif REPS % 2 == 0:
        count_down(short_brake_sec)
        print("Isteklo je vreme za rad..Vreme je za pauzu od 5min")
        label_timer.config(text="Pauza", fg = PINK)
    else:
        count_down(work_sec)
        print("Vreme je za rad! MOŽEŠ TI TO AKI")
        label_timer.config(text="Radi", fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60) #  --> daje najevci ceo broj 
    count_sec = int(count % 60) # --> daje samo ostatak, problem je sto daje samo jednu 0 ako nema ostatka
    if count_sec < 10:
        count_sec = "0" + str(count_sec) #! --> Dinamic typing: menjamo tip podatka ako menjamo varijablu, od integera na string
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # --> za promenu text u canvas koristimo ovo ovako....
    if count > 0:
       global timer 
       timer = window.after(1000,count_down, count-1)
    else:
        marks = ""
        work_session = math.floor(REPS/2) # --> jedna sesija je 20min rada + 5min pauze
        for _ in range(work_session):
            marks += "✔"
        label_checkmarks.config(text=marks)
        start_counting() # --> ako je ovo na vrhu onda pre svake pauze stavi ✔ a ako je ovde onda posle pauze.. to je zbog  REP += 1
        #! ovo ispod je za popup ali ne radi bas najbolje
        window.bell()
        window.deiconify()  # Unminimize the window
        window.lift()  # Bring the window to the front
        window.attributes("-topmost", 1)  # Make the window always on top of other windows
        window.after(500, lambda: window.attributes("-topmost", 0)) # Reset "always on top" behavior after 3000 milliseconds (3 seconds)
        window.focus_force()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk() 
window.title("Pomodoru Timer by WLQ") # --> title
window.config(padx=100, pady=50, bg=YELLOW)

# # .afetr () metoda koja ceka odredjeno vreme i onda funkciju koju smo dali izvsava i ima neogranicen (*args) broj argumenata
# def say_something(a,b ,c):
#     print(a)
#     print(b)
#     print(c)
# window.after(1000, say_something, "hello", 3, 5)

#! Canvas Widget
# Place image and text right on top of image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # --> gledamo koliko je slika velika pa prema tome
tomato_img = PhotoImage(file="Dan_28/tomato.png")
canvas.create_image(100, 112, image=tomato_img) # --> pola X, pola Y velicine i mora da se definise PhotoImage koji cita put do fajla koji ima sliku
#* napomena ako se ostavi x = 100, leva strana slike ce biti malo isecena, jer je pozicija slike suvise na levo, centrirana je na levo, tako da treba da stavimo onda malo vise od 100, tipa 102, ali ako se iskoristi highlightthickness=0 tacno se izgubi tih 2px i onda mozemo da ga vratimo na 100
timer_text = canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 24, "bold"), fill=GREEN) 
canvas.grid(row=1, column=1) # --> postavljamo sliku

# count_down(5) # --> mora da stoji ispod dela gde je definisan timer_text

#! LABEL TIMER
label_timer = Label(text = "Timer", font=(FONT_NAME, 32, "bold"), fg= GREEN, background= YELLOW, justify= "center")
label_timer.grid(row=0, column=1) # --> postavljamo tekst

#! LABEL CHECK MARKS
label_checkmarks = Label(text = "", font=(FONT_NAME, 24, "bold"), fg= GREEN, highlightthickness=0, background= YELLOW)
label_checkmarks.grid(row=3, column=1) # --> postavljamo tekst

#! BUTTONS
button_start = Button(text="Start".upper(), command=start_counting, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
button_start.grid(row=2, column=0) # --> postavljamo tekst
button_reset = Button(text="Reset".upper(), command=reset, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
button_reset.grid(row=2, column=2) # --> postavljamo tekst


window.mainloop() # --> radi sve dok ne kliknemo na X, ovo ide skroz na kraj koda
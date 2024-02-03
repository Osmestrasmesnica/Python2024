 #! PYTHON DAN 27

#! TKINTER, *args, **kwargs, Creating GUI Programs
from tkinter import * # --> * znaci sve klase (class) iz tkinter uzimas, ne moras ponaosob da ih pises posle u tekstu

#! Pravljenje prozora od tkintera i njegova konfiguracija
window = Tk()
window.title("Moj prvi GUI") # --> title
window.minsize(width=500, height=500) # --> velicina prozora
window.config(padx=200, pady=200) # --> dodavanje paddinga u window

#! Label
# moramo da je napravimo i da napisemo kako ce se prikazivata na ekranu
my_label = Label(text = "I am a label", font=("Arial", 24, "bold"))
my_label["text"]= "New text" # --> menjamo stari text
my_label.config(text = "Jos noviji tekst") # --> menjamo sve prethodne tekstove sa ovim sada
#! stavlja ga na sredinu, ovo je jako bitna metoda koja se koristi, procitati u dokumentaciji
my_label.pack()
#! pored pack() mozemo da koristimo za preciznije postavljanje na neku koordinatu place()
# my_label.place(x=0, y=0)
#! a moze i grid, da se zamisli grid na ekranu
#my_label.grid(column = 0, row = 0)

#! Button
# pravimo funkciju da slusamo kada se klikne dugme da se odradi nesto
def button_click():
    print("Kliknuli su ANKA I LEKA")
    new_text = input.get()
    my_label.config(text = new_text)

# Pozivanje akcije button_click() klikom na dugme
my_button = Button(text = "Click me", command=button_click) # --> command je ime funkcije a ne cela metoda tako da se pise bez zagrada
my_button.pack()

#! Entery / Input
input = Entry(width= 50, background='yellow')
input.insert(END, string="Placeholder text...")
print(input.get()) # --> uzimas input kao string
input.pack()

#!Text
text = Text(height=4, width=50)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#!Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=50, command=spinbox_used)
spinbox.pack()

#!Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#!Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#!Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#!Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Da bi prozor bio staolno otvoren i da bi slusao inpute od usera
# ovo u sustini menja while True: window.liste() petlju
# ovo uvek stoji na kraju koda skroz dole
window.mainloop()

# # ! Advanced Python Argumentas
# # Vecina funkcija vec ima zadatu pocetnu vrednost, i mi samo menjamo ono sto ne zelimo da bude deffault
# def my_function(a=1, b=2, c=3):
#     #Do this with a
#     #Then do this with b
#     #Finaly do this with c  

#! Kviz
#? Pitanje 1:
# What is the output of this code? 
def foo(a, b=4, c=6): 
    print(a, b, c)
foo(1)
# RESENJE: 1 4 6

#? Pitanje 2:
# What is the output of this code?
def foo(a, b=4, c=6): 
    print(a, b, c)
foo(4, 9)
# RESENJE: 4 9 6

#? Pitanje 3:
# What is the output of this code?
def foo(a, b=4, c=6): 
    print(a, b, c)
foo(1, 7, 9)
# RESENJE: 1 7 9

#? Pitanje 4:
# What is the output of this code?
def foo(a, b=4, c=6):
    print(a, b, c)
foo(20, c=6)
# RESENJE: 20 4 6 

#! Unlimited Arguments - *args
def add(*args): # --> obavezno * sto znaci da moze da se unese neogranicen broj argumenata
    for n in args: # --> loop kroz sve argumente
        print(n)

#! Many Keyworded Arguments - **kwargs
def calculate(n, **kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5) # --> ovo sad apretvara **kwarg u dictionary sa svojim keywords i starting values

#! KVIZ 2
#? Pitanje 1:
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
bar(1, 2)
# Resenje: 1 2 "yes please!" 0

#? Pitanje 2:
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
bar(toast='nah', spam=4, eggs=2)
# Resneje: 4 2 nah 0

#? Pitanje 3:
def test(*args):
    print(args)
test(1,2,3,5)
# What is the data type of args?
# Resenje: Tuple

#? Pitanje 4:
def test(*args):
    print(args)
test(1,2,3,5)
# What is output
# Resenje: (1, 2, 3, 5)

#? Pitanje 5:
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
all_aboard(4, 7, 3, 0, x=10, y=64)
# Resenje: 4 (7, 3, 0) {"x":10, "y":64}

#! pored pack moze da se koristi i place(x= , y=) da se postavi element na ekran preciznije od pack()
 #! Primer unlimited arguments
def add(*args):
    print(sum(args))
    print(args[1]) # --> posto je TUPLE args onda mozemo i da ga pronadjemo koji je po redu koji argument unutar args

add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#! Primer **kwargs

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"] # --> moze ovako ali bolje je da se dodat .get() pre toga, ovde ako se ne unese argumenta vraca se error
        self.year = kw.get("year") # --> kada ima get(), onda ako se ne unese ovaj argument vraca samo None
        self.seats = kw.get("seats")

moj_auto = Car(make="Volkswagen", model = "Passat B8", year = 2017) # --> nismo upisali seats ali posto ima get() nema errora

print(moj_auto.make)
print(moj_auto.model)
print(moj_auto.year)
print(moj_auto.make, moj_auto.model, moj_auto.year)

#! Napraviti tkinter sa gridom
from tkinter import *

window = Tk()
window.title("Moj prvi GUI") # --> title
window.minsize(width=500, height=500) # --> velicina prozora
window.config(padx= 100, pady=200) # --> dodavanje paddinga svim elementima u window


label = Label(text = "Neki Label")
label.grid(row = 0, column= 0)

button = Button(text = "Neki Button")
button.grid(row = 1, column = 1)

new_button = Button(text = "New Button")
new_button.grid(row = 0, column = 2)

input = Entry()
input.grid(row = 2, column = 3)



window.mainloop()
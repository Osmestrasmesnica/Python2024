# KONVERTER RSD TO CHF
from tkinter import *
import locale


window = Tk()
window.title("Konverter RSD u CHF by WLQ") # --> title
window.minsize(width=300, height=300) # --> velicina prozora
window.config(padx= 100, pady=100) # --> dodavanje paddinga svim elementima u window

entry = Entry(justify='center', width = 7)
# entry.insert(END, string="Unesite sumu..", )
entry.focus()
entry.grid(column= 1, row= 0)

locale.setlocale(locale.LC_ALL, '')

def format_currency(amount):
    return locale.format_string("%.*f", (2, amount), grouping=True)

def button_click():
    suma = float(entry.get())
    suma = suma * 0.0079827
    suma = round(suma, 2)
    label_converted.config(text=f"{format_currency(suma)}")

def RSD_to_CHF():
    suma = float(entry.get())
    suma = suma * 0.0079827
    suma = round(suma, 2)
    label_converted.config(text=f"{format_currency(suma)}")
    label_1.config(text=f"RSD")
    label_2.config(text=f"CHF")

def RSD_to_EUR():
    suma = float(entry.get())
    suma = suma * 0.00851986
    suma = round(suma, 2)
    label_converted.config(text=f"{format_currency(suma)}")
    label_1.config(text=f"RSD")
    label_2.config(text=f"EUR")
    button.config(command=RSD_to_EUR)

def CHF_to_RSD():
    suma = float(entry.get())
    suma = suma * 125.27
    suma = round(suma, 2)
    label_converted.config(text=f"{format_currency(suma)}")
    label_1.config(text=f"CHF")
    label_2.config(text=f"RSD")
    button.config(command=CHF_to_RSD)

def EUR_to_RSD():
    suma = float(entry.get())
    suma = suma * 117.37
    suma = round(suma, 2)
    label_converted.config(text=f"{format_currency(suma)}")
    label_1.config(text=f"EUR")
    label_2.config(text=f"RSD")
    button.config(command=EUR_to_RSD)


def CHF_to_EUR():
    suma = float(entry.get())
    suma = suma * 1.06728
    suma = round(suma, 2)
    label_converted.config(text=f"{format_currency(suma)}")
    label_1.config(text=f"CHF")
    label_2.config(text=f"EUR")
    button.config(command=CHF_to_EUR)

def EUR_to_CHF():
    suma = float(entry.get())
    suma = suma * 0.9369398
    suma = round(suma, 2)
    label_converted.config(text=f"{format_currency(suma)}")
    label_1.config(text=f"EUR")
    label_2.config(text=f"CHF")
    button.config(command=EUR_to_CHF)

label_1 = Label(text="RSD")
label_1.grid(column= 2, row= 0)

label_text = Label(text="u WLQ menjacnici je:")
label_text.grid(column= 0, row= 1)

label_converted = Label(text="0")
label_converted.grid(column= 1, row= 1)

label_2 = Label(text="CHF")
label_2.grid(column= 2, row= 1)

button = Button(text="Izračunaj", command=button_click)
button.grid(column= 1, row= 2, )

def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
    if listbox.get(listbox.curselection()) == valute[0]:
        if entry.get() != "":
            RSD_to_CHF()

    elif listbox.get(listbox.curselection()) == valute[1]:
        if entry.get() != "":
            RSD_to_EUR()
    elif listbox.get(listbox.curselection()) == valute[2]:
        if entry.get() != "":
            CHF_to_RSD()
    elif listbox.get(listbox.curselection()) == valute[3]:
        if entry.get() != "":
            EUR_to_RSD()
    elif listbox.get(listbox.curselection()) == valute[4]:
        if entry.get() != "":
            CHF_to_EUR()
    elif listbox.get(listbox.curselection()) == valute[5]:
        if entry.get() != "":
            EUR_to_CHF()

listbox = Listbox(height=6)
valute = ["RSD to CHF", "RSD to EUR", "EUR to RSD", "CHF to RSD", "CHF to EUR", "EUR to CHF"]
for valuta in valute:
    listbox.insert(valute.index(valuta), valuta)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column= 3, row=1)

window.mainloop()
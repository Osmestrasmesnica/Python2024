#PYTHON DAN 10
#! Functions with outputs
def my_function():
    result = 3*2
    return result # --> ovaj deo funkcije je output i on se obicno stavlja u varijablo i menja deo gde se poziva fukncija

my_function()

output = my_function() # --> sve posle return dela iz funkcije  je stavljano u ovu varijablu, ali sve sto je u tom redu
print(output)

#! Primer output funkcije
def format_name(f_name, l_name):
    ime = f_name.title() # --> title() funkcija za formatiranje stringa  da je svako prvo slovo veliko
    prezime = l_name.title()
    return f"{ime} {prezime}" # --> ovaj deo koda će zameniti deo koda gde se poziva funkcija

formatirano_ime = format_name("aleksa", "VLKU") # --> ovaj deo koda će se zameniti sa delom koji je u retrun

print(formatirano_ime)

#! Function with more than one argument
def format_name(f_name, l_name):
        if f_name == "" or l_name == "":
             return "Niste uneli dobro podatke" # --> mogucnost da se funkcija zavrsi ranije ako se ne unesu dobro podaci, printace se "None"
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()
        return f"{formated_f_name} {formated_l_name}"

print(format_name(input("Kako se zovete?"), input("Kako se prezivate?")))

#! Functions with Outputs
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  f"Result: {formated_f_name} {formated_l_name}"

#! Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
#or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))

#! Already used functions with outputs.
length = len(formatted_name)

#! Return as an early exit
def format_name(f_name, l_name):
  """Take a first and last name and format it
  to return the title case version of the name.""" # --> DOCSTRINGS, odnosno opis sta radi funkcija kada drzis preko nje
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"

#! VEŽBA 1
#In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.
# You are then going to modify a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)
# And it will use this information to work out if the year is a leap year and decide the number of days in the month, then return that as the output, e.g.:
# 28
# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.
# Hint
# Look at the function call at the bottom of the code to see the positional arguments. The order is very important.
# Feel free to choose your own parameter names.
# Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]
# Be careful with indentation.
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        #print("Leap year")
        return True
      else:
        #print("Not leap year")
        return False
    else:
      #print("Leap year")
      return True
  else:
    #print("Not leap year")
    return False
  
def days_in_month(selected_year, selected_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  
  if is_leap(selected_year) and selected_month-1 == 1:
    return month_days[selected_month-1] + 1 
  else:
    return month_days[selected_month-1]

year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

#! Docstrings
def format_name(f_name, l_name):
  """Take a first and last name and format it
  to return the title case version of the name.""" # --> DOCSTRINGS, odnosno opis sta radi funkcija kada drzis preko nje, moras da korstis """ na podcetku i na kraju...
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"

format_name()

#! Kviz
#? 1 - Sta ce biri ovde printovano
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

print(add(2, multiply(5, divide(8, 4)))) # --> 12.0

#? 2 - Sta ce ovde biti prinotvano
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result) # --> 15

#? 3 - Sta ce ovde biti prinotvano
def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25)) # --> None

#! RAZLIKA PRINTA I RETURNA


#! FINALE -- Calculator
#Sabiranje (Addition)
def sabiranje(n1, n2):
   return n1 + n2

#Oduzimanje (Subtraction)
def oduzimanje(n1, n2):
   return n1 - n2

#Množenje (Multiplication)
def mnozenje(n1, n2):
   return n1 * n2

#Deljenje (Division)
def deljenje(n1, n2):
   return n1 / n2

# Napraviti dictionary gde su key +, -, * , / a value su imena funkcija
operacija = {
    "+": sabiranje,
    "-": oduzimanje,
    "*": mnozenje,
    "/": deljenje
}

num1 = int(input("Koji je prvi broj?:\n"))
for key in operacija:
    print (key)
simpol_operacije = input("Izaberite matematičku operaciju koje je prikazana.\n")
num2 = int(input("Koji je drugi broj?:\n"))
prvi_odgovor = operacija[simpol_operacije](num1, num2)

#moze i ovako
#funkcija_racunanja = operacija[simpol_operacije]
#prvi_odgovor = funkcija_racunanja(num1, num2)

print(f"{num1} {simpol_operacije} {num2} = {prvi_odgovor}")

simpol_operacije = input("Izaberite sledeću matematičku operaciju:")
num3 = int(input("Koji je sledeći broj?:\n"))
funkcija_racunanja = operacija[simpol_operacije]
drugi_odgovor = funkcija_racunanja(prvi_odgovor, num3) # --> ako ostavimo ovo u zagradi kao funkcija_racunanja(num1, num2), num3 dobice se num1, num2, num3 i pogresno ce se izracunati npr dobice se 2+3*3 = 18 a ne (2+3)*3 = 15
print(f"{prvi_odgovor} {simpol_operacije} {num3} = {drugi_odgovor}")

poslednji_rezultat = 0

dalje = input("Upišite 'da' ako želite da nastavite da računate sa brojem {poslednji_rezultat} ili 'ne' ako ne želite da nastavite da računate")


# smanjiti kod i omoguci da mozes i sledeci broj da dodas ako se upise da, a da izadjes ako se upise ne
# pisacu ceo kod opet da moze lakse da se kopira

#Sabiranje (Addition)
def sabiranje(n1, n2):
   return n1 + n2

#Oduzimanje (Subtraction)
def oduzimanje(n1, n2):
   return n1 - n2

#Množenje (Multiplication)
def mnozenje(n1, n2):
   return n1 * n2

#Deljenje (Division)
def deljenje(n1, n2):
   return n1 / n2

# Napraviti dictionary gde su key +, -, * , / a value su imena funkcija
operacija = {
    "+": sabiranje,
    "-": oduzimanje,
    "*": mnozenje,
    "/": deljenje
}

num1 = int(input("Koji je prvi broj?:\n")) #--> bolje ovo da je float a ne integer

def dalje_operacija():
    for key in operacija:
        print (key)
    simbol_operacije = input("Izaberite matematičku operaciju koje je prikazana.\n").lower()
    num2 = int(input("Koji je sledeći broj?:\n"))
    funkcija_racunanja = operacija[simbol_operacije]
    rezultat = funkcija_racunanja(num1, num2)
    print(f"{num1} {simbol_operacije} {num2} = {rezultat}")
    return rezultat

rezultat = dalje_operacija()
ponavljanje = True

while ponavljanje:
    dalje = input(f"Upišite 'da' ako želite da nastavite da računate sa brojem {rezultat} ili 'ne' ako ne želite da nastavite da računate?\n")

    if dalje == "da":
        num1 = rezultat
        rezultat = dalje_operacija() # --> nemoj ovaj deo da zaboravis 
    elif dalje == "ne":
        print(f"Vaš rezultat je: {rezultat}")
        ponavljanje = False
    else:
        print("Unesite ispravnu komandu sledeći put. Sada morate sve ispočetka jer ne znate da pratite uputstva...:)")

#? KURS VERZIJA
import os
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      os.system('cls')
      calculator()

calculator()

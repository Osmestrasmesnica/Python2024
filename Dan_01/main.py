#PYTHON DAN 1
#! 1 - VEŽBA
# Nauci kako se koristi print()
# Mozes da koristis "" ili '' , ali uvek vodi racuna da u tekstu negde nemas tih apostrofa jel ce prepoznati prvi u tekstu i iskljucice funkciju
print('Day 1 - Python Print Function')
print("The function is declared like this:")
# Ako u tekstu imas "" onda mozes da koristis '' i obrnuto
print("print('what to print')")
#ako u tekstu postoji ' i "" onda koristis ''' ''' i u okviru toga mozes sve da koristis
print('''Aleksa said:"This is biggest invetion of Stevan's life so far"''')

#! 2 - VEŽBA
# Kako da nađeš greške u kodu i da ih središ
# Fix the code below 👇
# Answer part 1. Missing double quotes before the word Day.
# print(Day 1 - String Manipulation")
print("Day 1 - String Manipulation")
# Answer part 2. Outer double quotes changed to single quotes.
# print("String Concatenation is done with the "+" sign.")
print('String Concatenation is done with the "+" sign.')
# Answer part 3. Extra indentation removed
#   print('e.g. print("Hello " + "world")')
print('e.g. print("Hello " + "world")')
# Answer part 4. Extra ( in print function removed.
# print(("New lines can be created with a backslash and n.")
print("New lines can be created with a backslash and n.")

#! 3 - VEŽBA
# Izračunati dužinu STRINGA koristeci funkciju len() za input()
print(len(input()))

#! 4 - VEŽBA 
# Zameniti vrednosti varijabli, ovo verovatno moze jos na neki nacin da se uradi
# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
c = a
a = b
b = c

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
# Ako hoces i mnozenje da radis odna moras da dodas int() pre toga jer je ovo pre toga sacuvano kao string tj kao karakter a ne kao broj
print("ovo je sada mnozenje u nastavku: " , "\n" , int(a) * int(b))

#! FINALE ZA DANAS 'BAND NAME GENERATOR'
#1. Create a greeting for your program.
print("Dobrodošli u našu muzičku kuću! Zanima nas kako se zove Vaš bend i da li Vam treba pomoć oko imena?\n")
#2. Ask the user for the city that they grew up in.
grad = input("Unesite grad gde ste rođeni: \n")
print(grad)
#3. Ask the user for the name of a pet.
ljubimac = input("Unesite ime vašeg ljubimca: \n")
print(ljubimac)
#4. Ask the user for childhood nick name.
nadimak = input("Unesite Vaš nadimak koji ste imali kada ste bili mali: \n")
print(nadimak)
#5. Combine the name of their city and pet and show them their band name.
print("Ime vašeg benda bi moglo da bude: " + nadimak + " " +  ljubimac + " " + grad)
#6. Make sure the input cursor shows on a new line: - ovo se radi dodavanjem \n na kraju

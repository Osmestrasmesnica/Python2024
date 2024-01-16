#PYTHON DAN 2
# DATA TYPE
#! String
# Stavljaju se uvek u navodnike ', "", ''' '''
# Ako želimo neki broj iz stringa da uzmemo onda stavljamo [] - Subscripting
print("Hello"[1])
# Ako je integer onda ga moramo prebaciti u string koristeci funkciju str()
print(len("Aleksa7Vlku12"))
print(len(str(1234567891011121314151617181920)))
# Za string ne rade matematičke operacije
print("123" + "345") #ovo je string pošto su unutar "" tako da se samo spaja i rezultat je -> 123345

#! Integer
# Svi celi brojevi su integer
# Kada pišeš ovaj tip podataka onda ti ne treba "" i onda rade matematičke operacije
print(123 + 456)
# Kada pišeše velike brojeve , ili . možeš zameniti u kodu sa _ npr. 1.123.421/1,123,421 može se uneti kao 1_123_432
print(123_456_789)

#! Float
# Brojevi sa decimalnim zapisom
# Koristiš type() funkciju da odrediš koji je tip podatka
print(3.14159)
print(type(3.14159))  # Float type

#! Boolean
# Imaju samo True ili False

#! Menjanje tipa podataka pomoću funkcija str(), int(), boolean(), float()
# Prilikom korišćenja funkcije len() dobijamo tip podatka integer koji ne možemo da spajamo sa integer tipom podatka kada printujemo
num_char = len(input("Kako se zoveš?\n"))
print(type(num_char)) # --> integer

new_num_char = str(num_char) # --> pretvaranje u string
print(type(new_num_char)) # --> string
print("Tvoje ime ima "+ new_num_char + " karaktera u nazivu")

#! Uzimanje pozicije u stringu sa [] i brojanje kreće od 0
street_name = "Abbey Road"
print(street_name[4] + street_name[7])  # --> yo

#! 1 - VEŽBA
#  Od broja koji je u inputu uzme cifre i saberi ih
two_digit_number = input("Unesi neki dvocifren broj:")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
position1 = two_digit_number[0]
position2 = two_digit_number[1]
print("Type of position1:", type(position1), "| Type of position2:", type(position2)) # --> tip je string i mora da se pretvori u integer
sum = int(position1) + int(position2)
print("Suma cifara u dvocifrenom broju je:", sum)

#! Matematičke operacija u Pythonu
# Rezultati matematičkih operacija su uvek u format tipu float
# sabiranje 3 + 5
# oduzimanje 7 - 3
# množenje 3 * 2
# deljenje 6 / 3 --> rezultat je ovde 2.0
# stepenovanje 2 ** 3
# samo ostatak da se prikaže 9 % 4 --> 1
# samo deo koji nije ostatak, ceo broj 9 % 4 --> 2
# ako ima više operacija u redu PEMDASLR --> redosled je (), **, * i /, + i -, od leva na desno
print(3*3+3/3-3) # --> 7.0
print(3*(3+3)/3-3) # --> 3.0

#! 2 - VEŽBA
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# 1st input: enter height in meters e.g: 1.65
height = input("Unesi visinu u metrima sa . kao razmakom: \n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Unesi težinu u kilogramima: \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = round(float(weight) / float(height)**2, 2)
print(type(bmi))
print("Vaš BMI je:", bmi)
print("Vaš BMI je:", int(bmi))

if bmi < 18.5:
    print("Pothranjenost")
elif 18.5 <= bmi < 24.9:
    print("Normalna ili zdrava telesna masa")
elif 25.0 <= bmi < 29.9:
    print("Prekomerna telesna masa")
elif bmi >= 30:
    print("Gojaznost")

#! Zaokruživanje brojeva
# Ukoliko samo napišemo int() za neki float, on će samo uzeti ceo broj
print(8/3) # --> 2.666666
print(int(8/3)) # --> 2
print(round(8/3)) # --> 3
print(round(8/3,2)) # --> 2.67
print(8//3) # --> 2 i rezultat je integer  sto znači da je isto sto i int(8/3)
print("{:.2f}".format(8/3)) # --> 2.67, ovo kruzi na dve decimale iako je posle prve 0, npr 2.30 dok round() to ne radi

#! Matematičke operacije na već postojeću varijablu bez ponavljanja ista
rezultat = 8*2
print(rezultat) # --> 16
rezultat += 2
print(rezultat) # --> 18

#! f-String
# dodaje se f pre "", '', ''' '''
# Koristimo kada zelimo u funkciji da koristimo i string i integer i sve oblike podataka bez da pisemo stalno + ili da ih prebacujemo funkcijama int(), str() ...
# Za ubacivanje stvari koje nisu string koristimo zagrade {} i unutra ubacujemo tipove podataka
godine = int(input("Unesite koliko godina imate godina:"))
print(f"Imam {godine} godina, a za 18 godina ću imati {godine + 18}")

#! 3 - VEŽBA
# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
weeks_in_1year = 52
# print(type(age)) --> pošto je str tip, moramo ga prebaciti u integer
weeks = (90 - int(age))*weeks_in_1year 
print(f"You have {weeks} weeks left.")

#TODO KVIZ
# 1 - Koji je rezultat ovde
# print(6 + 4 / 2 - (1 * 2)) # --> 6.0 

# 2 - Data type od a je
# a = int("5") / int(2.7)
# print(type(a)) # --> float

# 3 - Linija koda sa greskom
# age = 12
# print("You are " + age  + " years old")

#! FINALE ZA DANAS - TIP CALCULATOR
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Write your code below this line 👇

print("Dobrodošao u program koji izračnuva koliku napojnicu bi trebalo da date konobaru!")
račun = float(input("Unisite koliko je iznosio račun: \n"))
napojnica_procenti = (float(input("Koliku napojnicu želite da ostavite? 5%, 10%, 12% ili neku drugu?\nUnesite procentualnu visinu napojnice:")) / 100) #napojnica je u procentima
napojnica = račun * napojnica_procenti
napojnica_2decimale = "{0:.2f}".format(napojnica)

print(f"Visina napojnice treba da bude {napojnica_2decimale}")

broj_ljudi = int(input("Unesite koliko ljudi deli račun: \n"))

plaćanje = (napojnica + račun) / broj_ljudi

ceh = round(plaćanje, 2)
ceh_uvek2decimale = "{:.2f}".format(plaćanje) # --> zapamtiti ovo za 2 decimale "{:.2f}".format
print(f"Svako treba da plati {ceh} dinara, odnosno {ceh_uvek2decimale} dinara")

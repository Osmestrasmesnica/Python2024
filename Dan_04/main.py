#PYTHON DAN 4
# Randomisation and Python lists
#! RANDOM NUMBER, MODULE
# kada imamo neke module i hocemo da ih koristimo, onda moramo da ih importujemo na pocetku
# mozemi i samo da pravimo module u drugim fajlovima pa da ih importujemo na pocetku
# koristimo random. da generisemo random neke stvari

#importovanje modula
import random #ovo je module, i napravio ga je python tim da bi nam olaksao da stvaramo random stvari
import  new_module #ovo je module koji smo sami napravili, ovako imoporujemo i onda možemo da koristimo sve iz njega

# random celi brojevi
random_integer = random.randint(1,10) # u ovom slučaju stvaramo random integer (cele brojeve), u zagradi je raspon uključujući i te brojeve
print(random_integer)

# import modula
print(new_module.pi) # ovako se unose iz nekog drugog modula neke stvari, prvo koristimo import i onda se ovako pozivamo na konkretnu stvar npr varijablu

# random decimalni borjevi od 0 do 1
random_float = random.random() # ovo je module za stvaranje random broja izmedju 0 i 1 ali ne ukljucuje 1
print(random_float)

# random decimalni brojevi od 0 do 5 ali ne i 5
randomFloat = random.random() * 5 # mnozimo sa tim brojem do koga zelimo
print(randomFloat) 

# primer random_love_score
love_score = random.randint(1,100)
print(f"You're love score is {love_score}")

#! 1 - VEŽBA
# GLAVA/PISMO
# Napraviti program koji ce generisati random brojeve 0 ili 1, ako je 0 onda je "Tails" a ako je 1 onda je "Heads"

# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

glava_ili_pismo = random.randint(0,1)
if glava_ili_pismo == 1 :  #! ne znam zasto ne radi ako ovde stavim == 0
  print("Heads")
else :
  print("Tails")

#! Data Structure - Offset and Appending Items to Lists
# liste se pišu sa [] zagradama, i unutra mogu biti svi tipovi podatak i string i integer i ostali... npr fruits = ["Jabuka", "Jagoda", "Kruska"]
# redosled u listi je redosled kojim je dodavano, odnosno sa leva na desno, od starijeg ka mladjem/novijem
# liste krecu od broja 0, a ne od broja 1
# ako hocemo da print neki konretan item u nizu, npr hocemo da printamo koji je 3. item u nizu onda koirstimo [2], opet koristimo [] zagrade
# moze se koristiti i negativan broj [-1] i to je poslednji item u nizu
# ako hocemo da menjamo item u nizu, biramo koji je u nizu [] npr lista[2] = "kako_hocemo_da_menjamo"
# ako hocemo da dodamo nesto novo na niz koirsimo funkciju .append
# pored ove funkcije mozemo jos da koristimo .extend () dodaje svaki elemnt liste u vec postojecu listu kao pojedinacne listove, za razliku od appenda koji bi dodao elemnte sve zajedno kao jednu listu, .insert(i, x) i je indeks itema pre koga zelimo da ubacimo nov item, x je sta zelimo da unesemo, .remove(x) brisanje prvog elementa sa ovim vrednostima iz liste, .clear() sve elemente brise iz liste, .count(x) broji koliko puta se x ponavlja u listi, sort(*, key=None, reverse=False) za sortiranje... 
states_of_america = ["Delaware", "Pennsylvania"]
print(states_of_america[1])
states_of_america[1]= "Majdanpek" # hocemo da zamenimo na drugoj poziciji sta je bilo sa ovim sto ovde sada pisemo
print(states_of_america[1])
print(states_of_america)
states_of_america.append("Bor") # dodali smo na niz "Bor"
print(states_of_america)

#? SUŠTINA JE DA NE PAMTIŠ SVE OVE FUNKCIJE VEĆ DA PROČITAŠ DOKUMENTACIJU I DA AKO ZNAŠ DA JE NEŠTO MOGUĆE DA TO PRONAĐEŠ NA NETU U DOKUMENTACIJIž

#! 2 - VEŽBA 
# RANDOM NAME FROM LIST OF NAMES
# write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random
print("Unestie imena ljudi ispod, i nasumično će se izabrati osoba koja pere sudove...nrp. Aleksa, Ankica, Vuk...")
names_string = input()
names = names_string.split(", ") # splits the string names_string into individual names and puts them inside a List called names
# print(names) # list
broj_ljudi = len(names) # broj elemenata u listi
# print(type(broj_ljudi))
broj_ljudi_lista = broj_ljudi - 1 # oduzimas 1 zato  sto brojanje krece od 0 a ne od 1
ko_pere_sudove = random.randint(0, broj_ljudi_lista) # izlacenje random pozicije elementa u listi
print(f"{names[ko_pere_sudove]} danas pere sudove!") # printanje naziva pozicije koje je izvuceno

#! IndexError
# Error koji se pojavljuje ako iskoristis len() i posle toga uzmes to kao index npr... lista[len()] jer ce len uzeti od 1 do i a lista ide od 0 do i... tj index je len() - 1

#! NestedList
# spajanje dve ili vise lista, i ima [] [] onoliko koliko ima lista
voće =["jagoda", "nektarina", "jabuka", "grožđe", "breskva", "višnja", "kruška"]
povrće = ["spanać", "kelj", "paradajz", "celer", "krompir"]

prljavi_plodovi = [voće, povrće] # --> [["jagoda", "nektarina", "jabuka", "grožđe", "breskva", "višnja", "kruška"], ["spanać", "kelj", "paradajz", "celer", "krompir"]]


#TODO KVIZ
# 1 - Given the following list:
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# Which line of code will give you "Apples"?
# fruits[-5]

# 2 - Given the code below:
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)
# What do you think will be printed?
# ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Melons", "Lemons"]

# 3 - Given the code below:
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1]) # --> ovde se gleda ovako, ako ima dve liste, gleda se druga lista (to je prva[]) i iz te liste index 1 (to je druga ova [])
# What will be printed?
# "Kale"

#! 3 - VEŽBA 
# Treasure Map
# You are going to write a program that will mark a spot on a map with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what it looks like, notice the nesting:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# Now it looks a bit more like the coordinates of a real map:
# Your job is to write a program that allows you to mark a square on the map using a letter-number system.
# So an input of A3 should place an X at the position shown below:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['x', '⬜️', '⬜️']
# First, your program must take the user input and convert it to a usable format.
# Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
# function .index(x) vraca na kom indeksu tj na kojoj poziciji se nalzi x u listi

#! Verzija ALEKSA
print("Hiding your treasure! X marks the spot.")
print("Uneti polje u kome ce biti `x`")
print("Uneti prvo slovo A, B ili C pa onda broj 1, 2 ili 3... primer A1 /// C3 /// B2...")
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
#print(f"{line1}\n{line2}\n{line3}")

slovo = position[0] # --> u veziji sa kursa ovo pretvaraju u indeks isto, uvek je bolje da se sve pretvori u isti oblik, manje koda se pise
broj = int(position[1])

if slovo == "A" :
  map[broj-1][0] = "X"
elif slovo == "B" :
  map[broj-1][1] = "X"
elif slovo == "C" :
  map[broj-1][2] = "X"
else :
  print("Neispravan polje! Blago Vam nije ovde zakopano")
print(f"{line1}\n{line2}\n{line3}")

#! Verzija KURS
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X" # --> seti se samo da prvo ide spoljna lista pa unutrasnja kada je ovo u pitanju [][]

print(f"{line1}\n{line2}\n{line3}")

#! FINALE ZA DANAS - KAMEN PAPIR MAKAZE
#! ********************************************************************
#! VERZIJA ALEKSA
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("Da li smeš protiv kompjutera da igraš KAMEN PAPIR MAKAZE u to ko pere sudove????")
print("********************************************************************")

#KORISNIK
print('''Izaberi "Kamen" tako što ćeš napisati 0, "Papir" tako što ćeš napisati 1 ili "Makaze" tako što ćeš napisati 2''')
korisnički_unos = int(input())

if korisnički_unos == 0 :
    print(f"Izabrali ste: {rock}")
elif korisnički_unos == 1 :
    print(f"Izabrali ste: {paper}")
elif korisnički_unos == 2 :
    print(f"Izabrali ste: {scissors}")
else :
    print("Neispravan unos! Vama očigledno treba nekoliko puta pravila da se ponavljaju. Pročitajte opet šta treba da unesete....")

#KOMPJUTER
pc_unos = random.randint(0,2)

if pc_unos == 0 :
    print(f"Kompjuter bira: {rock}")
elif pc_unos == 1 :
    print(f"Kompjuter bira: {paper}")
elif pc_unos == 2 :
    print(f"Kompjuter bira: {scissors}")

print("***********************************************************")

#PRAVILA
# dva ista
if korisnički_unos == pc_unos : 
   print("Izjednačeno je... Igrajte ponovo ili igrajte sa Lekom :P")
# kamen papir
elif korisnički_unos == 0 and pc_unos == 1 :
   print("Izgubili ste... Nađite rukavice i počnite da perete sudove :)")
# kame makaze
elif korisnički_unos == 0 and pc_unos == 2 :
   print("Pobedili ste...Nađite Leku i zamolite ga da opere sudove jer su vam prsti otečeni od borbe KAMEN PAPIR MAKAZE :)")
# papir kamen
elif korisnički_unos == 1 and pc_unos == 0 :
   print("Pobedili ste...Pronađite neki izgovor što Leka treba da pere sudove :)")
# papir makaze
elif korisnički_unos == 1 and pc_unos == 2 :
   print("Izgubili ste... Smislite kako možete Leku da zamolite da on pere sudove umesto Vas :)")
# makaze kamen
elif korisnički_unos == 2 and pc_unos == 0 :
   print("Izgubili ste... Mislim red je da VI perete sada sudove... Dokle više Leka....")
# makaze papir
elif korisnički_unos == 2 and pc_unos == 1 :
   print("Pobedili ste...Ali mislim da je korektno ko najvise sudova pravi da i pere :)")
else :
   print("Neispravan unos! Vama očigledno treba nekoliko puta pravila da se ponavljaju. Pročitajte opet šta treba da unesete....")

#! ********************************************************************
#! VERZIJA KURS
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors] #! ovo je bas dobar način da se reše ove slike

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")





##Debugging challenge:
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: 

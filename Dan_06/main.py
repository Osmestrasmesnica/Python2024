#PYTHON DAN 6
#! Functions
#! Pravljenje nase fukncije

def moja_funkcija(): #koritimo def pa naziv_funkcije() i : na kraju i onda ispod uvuceno je sve sto se nalazi u funkciji
  print("Hello")
  print("Bye")

moja_funkcija() # --> pozivanje funckije kojoj ne treba input tj ima samo prazne ()

# igrica za funkcije 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

#u okviru igrice sam pravio ove funkcije da skratim kod i da olaksam citljivost
# def turn_right() :
#     turn_left()
#     turn_left()
#     turn_left()
# def turn_around() :
#     turn_left()
#     turn_left()
# #da napravi mali kvadratic
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()
#sledeci zadatak je da se napravi f-ja jump
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# jump 
# jump 
# jump 
# jump 
# jump 
# jump 

#A moze i ovako
# for step in range(6):
#   jump() 

#! Indentation
# voditi računa šta je uvučeno a šta ne
# ono što je uvučeno to se nalazi unutar funkcije
# ono što je napolju to nije u funkciji i nezavisno je
# voditi racuna na if elif, for petlje i ostale stvari koje isto koriste indentaciju
# koristiti tab ili 4 " " spejsa

# sajt gde su pravila za python
# https://peps.python.org/pep-0008/

#!KVIZ
# 1 - Which version of code will produce an Indentation Error when it is run?
# def my_function():
# print(my_function) --> nepravilano definisana funkcija, nema indentacije ovde
# 2 - Which version of code will output "This will run"?
# def my_function():
#     print("This will run")
# my_function() --> pravilno napisana funkcija
# 3 - In which version of code, will you see "This will run" printed?
# def my_function():
#   a = 3
#   if a > 2 :
#       print("This will run")
# my_function()

#!WHILE Loops
# nastavlja da se koristi petlja dok je uslov tacan

#! za prošli zadatak za robota uradio sam sa for petljom a ovako bi izgledalo sa while
# broj_prepreka = 6
# while broj_prepreka > 0:
#   jump()
#   broj_prepreka -= 1
#   print(broj_prepreka)

#! sa uslovom at_goal()
# while at_goal() != True:
#   jump() 
# while not at_goal(): # --> ovo moze da se napise i ovako kao negacija
#   jump()

#! prepreke koje se menjaju i nisu na istom mestu
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

#! prepreke koje su razlicine visine i razlicitog mesta
#! REŠENJE ALEKSA
# while not at_goal():
# #    while not wall_in_front(): --> ovo izbaciti i ubaciti umesto ovoga samo else: move() ispod ovog if
# #       move()
#     if wall_in_front():
#         turn_left()
#         while wall_on_right():
#             move()
#         turn_right()
#         move()
#         turn_right()
#         while not wall_in_front():
#             move()
#         turn_left()
#     else:
#         move()
#! REŠENJE KURS
# ovde je samo definisano jump() da je ovo sto sam ja gore napisao... BRAVO ALEKSA!!!
# def jump():
#   turn_left()
#   while wall_on_right():
#       move()
#   turn_right()
#   move()
#   turn_right()
#   while not wall_in_front():
#       move()
#   turn_left()
#
# while not at_goal():
#   if wall_in_front():
#       jump()
#   else:
#       move()

#! FINALE ZA DANAS - REŠENJW ZA LAVIRINTE
#! ********************************************************************
#! VERZIJA ALEKSA
# Reeborg was exploring a dark maze and the battery in its flashlight ran out.
# Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.
# What you need to know
# The functions move() and turn_left().
# Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
# How to use a while loop and if/elif/else statements.
# It might be useful to know how to use the negation of a test (not in Python).
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
# može da se desi da uđeš u infinity loop kada ti je uvek slobodno desno i onda ces se vrteti u krug....
# ovako sam to ja resio
# def turn_right() :
#     turn_left()
#     turn_left()
#     turn_left()

# i = 0
    
# while not at_goal():
#     if right_is_clear() and i < 4:     
#         turn_right()
#         move()
#         i += 1
#     elif front_is_clear():
#         move()
#         i = 0
#     else:
#         turn_left()
#         i = 0

#! VERZIJA KURS
# def turn_right() :
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#   move()
# turn_left()

# while not at_goal():
#     if right_is_clear() and i < 4:     
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
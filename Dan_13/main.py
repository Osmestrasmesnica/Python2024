#PYTHON DAN 13
#! Debugging

############DEBUGGING#####################

# Describe Problem
# uvek je pametno da se opise problem i da se tako pronadje bug
# def my_function():
#   """This function is used to check range from 1 to 19 and to print 'You got it' when number is 20"""
#   for i in range(1, 20+1): # --> do 20+1 popraviti
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) # --> ovde dobijes integer od 1 do 6 prepraviti na od 0 do 5
# print(dice_imgs[dice_num]) # --> indexi so od 0 do 5 a ne od 1 do 6

# # Play Computer
# # otvori Thonny i gledaj redosled kojim se izvrsava kod i prati sta nije dobro
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994: # --> mora da se stavi i 1994 vece od jednako
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# # Prati sta ti izbacuje kao errore
# age = input("How old are you?")
# if int(age) > 18:
#     print(f"You can drive at age {age}.")

# # Print is Your Friend
# # Koristi print()
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # --> == poredi vrednost a = dodeljuje
# print(pages)
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# # Debugger Thonny, Python tutor...
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item) # --> ovo treba da bude unutar for petlje
#   print(b_list)

# mutate([1,2,3,5,8])

# Napravi pauzu
# Pitaj nekoga da ti pojasni
# Pitaj ChatGPT
# StackOverflow
# Pokreci kod posle svake male promene, nemoj da cekas da napises ceo program pa tek onda da ga run-ujes

#! VEŽBA 1
# Pronadji bag
number = int(input()) # Which number do you want to check?

if number % 2 == 0: # --> stajao je ovde =, sto znaci da mu je dodeljena vrednost bila
  print("This is an even number.")
else:
  print("This is an odd number.")

#! VEŽBA 2
# Pronadji bag
# Which year do you want to check?
#year = input()
year = int(input()) # --> treba u integer da se prebaci ovo 

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
#! VEŽBA 3
# Pronadji bag
target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0: # --> and a ne or
    print("FizzBuzz")
  elif number % 3 == 0: # --> elif a ne if
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number) # --> number a ne [number]

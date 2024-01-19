#PYTHON DAN 10
#! Scope
################### Scope ####################

# funkcija stvara local scope
# if statement, while loop i sve stvari koje se zavrsavaju sa : a uvucene su sa TAB ne stvaraju local scope

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

################### Local Scope ####################

def drink_water():
  water = 10
  print(f"Popio si {water} čaša vode danas...")

drink_water()
#print(water) # -->izbacuje NameError: name 'water' is not defined. 

################### Global Scope ####################

player_health = 10

def drinking_potion():
  potion_strength = 12
  print(player_health) # --> ovo moze da se poziva u funkciji zato sto je definisano kao globalna varijabla
  print(potion_strength)

drinking_potion()

# NAMESPACE -- ovaj princip se vazi i na funkcije i na sve
# Uvek treba voditi racuna gde definises sta

#! There is no Block Scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

# ako je if
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy) # -->printa se ovo 

# ako je funkcija
def create_enemy():
  if game_level < 5:
    new_ene = enemies[0]

#print(new_ene) # -->ne printa se ovoprinta se ovo jer nije 

#mora ovako da se napise
def create_enemy():
  if game_level < 5:
    new_ene = enemies[0]
  print(new_ene)

#! Modifikacija globalne varijable --> GLOBAL

enemies = "1"

# nacin broj 1
def increase_enemies():
  global enemies # --> mora ovako da se definisie da bi spoljasnju varijablu moga da menjas u local scope
  enemies = "2"
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# nacin broj 2
enemies2 = 3

def increase_enemies():
  print(f"enemies inside function: {enemies2}")
  return enemies2 + 1

enemies2 = increase_enemies()
print(f"enemies outside function:{enemies2}")

#! Globalne konstante

# Pisu se sa svakim velikim slovo, sto treba da nam znaci da ih ne diramo u local scope
# Najcesce su to neke konstante koje se ne menjaju kao npr.
 
PI = 3.14159
URL = "https://www.udemy.com/course/100-days-of-code/learn/lecture/19846106#questions"

#! KVIZ
# 1 - What will be printed in the console when the following code is run?
# DO NOT run the code, just pretend to be a computer.
# def a_function(a_parameter):
#     a_variable = 15
#     return a_parameter
# a_function(10)
# print(a_variable)
# --> dobije se NameError jer je a_variabla definisana u localnom scope

# 2 - What will be printed in the console when the code is run?
# DO NOT run the code, just pretend to be a computer.
# i = 50
# def foo():
#     i = 100
#     return i
# foo()
# print(i)
# --> dobije se 50, to je varijabla koja je definisana globalno

# 3 - What will be printed in the console when the following code is run?
# DO NOT run the code, just pretend to be a computer.
# def bar():
#     my_variable = 9
 
#     if 16 > 9:
#       my_variable = 16
 
#     print(my_variable)
# bar()
# --> rezultat je 16, u phytonu ne postoje block scope, unutar if/else/fore/while je isto kao i da je spolja varijabla

#! FINALE - The Number Guessing Game
#? KURS VERZIJA
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()


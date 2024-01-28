 #! PYTHON DAN 21
#! Inheritance and Slicing
#! Snake game part 2 - detect collision with food/with wall/tail and create scoreboard

#!Inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breath(self):
        print("Inhale, exhale")

class Fish(Animal): # u zagradi pisemo ako nasledjuje nesto iz druge clase
    def __init__(self):
        super().__init__() # kada dodamo super().__init__ onda nasledjujemo sve od super clase odnosno od klase koje je gore u zagradi, u ovom slucaju Animal... supper() moze da se doda ali nije neophodno

    def breath(self):
        super().breath() # kada dodamo super().breath() onda nasledjujemo sve sto ta metoda ima i plus mozemo da je modifikujemo
        print("Doing this under water")
        print("Dodatno nesto izmenjeno")

    def swim(self):
        print("Move in water.")

nemo = Fish()
nemo.swim()
nemo.breath()

#! KVIZ

#? Question 1:
# Given the following:

# class Dog:
#     def __init__(self):
#         self.temperament = "loyal"
 
#     def bark(self):
#         print("Woof, woof!")
# How do you create a class called Labrador (the subclass) that inherits from the Dog class (the superclass)?

# class Labrador (Dog):
#   def __init__(self):
#       self.temperament = "friendly"
# Correct. The call to super() in the initialiser is recommended, but not strictly required.

#? Question 2:
# Given this:

# class Dog:
#     def __init__(self):
#         self.temperament = "loyal"
 
# class Labrador(Dog):
#     def __init__(self):
#         super().__init__()
#         self.temperament = "gentle"

# What will this code print?

# doggo = Dog()
# print(f"A dog is {doggo.temperament}")
 
# sparky = Labrador()
# print(f"Sparky is {sparky.temperament}")

# A dog is loyal
# Spary is gentle

#? Question 3:
# Given this code:

# class Dog:
#     def __init__(self):
#         self.temperament = "loyal"
 
#     def bark(self):
#         print("Woof, woof!")
 
# class Labrador(Dog):
#     def __init__(self):
#         super().__init__()
#         self.is_a_good_boy = True
 
#     def bark(self):
#         super().bark()
#         print("Greetings, good sir. How do you do?")

# What will this print?

# sparky = Labrador()
# sparky.bark()

# Woof, woof!
# Greetings, good sir. How do you do?

# Correct. We are extending the functionality of the bark() method.

#! Nakon part1 nastavljamo sa pravljenjem igrice SNAKE

#! Napraviti klasu calss Food i da se pojavljuje random na ekranu u okviru 600x600 ekrana

#! Detect collision with food
# prepoznati kada se positiong food i head srednu
# skor povecati kada se ovo desi
# dodati jos jedan segment u duzini zmije

#! Create a scoreboard that updates when you collide with food
# za ovo koristimo write(), i clear()

#! Detect collision with wall
# ako udarsi onda cemo da printamo "Game Over"
# napraviti if funkciju za detektovanje da li glava zmije prelazi odredjenu poziciju x ili y

#! Detect collision with tail and make it extend when you collide with food
# napraviti funkciju za ekstenziju
# napraviti funkciju za udaranje sa repom

#! SLICING
# ako hocemo samo deo iz liste da uzmemo koristimo slice
# slicing radi u u tuples i u listama

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "sol", "la", "si")

print(piano_tuple[1:]) # od pozicije koju si selektovao do kraja
print(piano_keys[:4]) # sve pre toga do pozicije 3, odnosno 4-1
print(piano_tuple[2:5]) # ako hoces od mi do sol onda pises ovako, poslednja cifra se je -1, brojanje u listi krece od 0 a nama treba od 2 do 4 onda pisemo, [2:5], posto je 5-1 = 4
print(piano_tuple[:7:3]) # ako dodamo i 3. broj u zagradi onda je to step, svaki 2 ce se slice uraditi
print(piano_keys[::2]) # u celoj listi uzece se svaki drugi element
print(piano_keys[::-1]) # dace ti celu listu od poslednjeg elementa do prvog sortirano



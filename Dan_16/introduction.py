# #! #PYTHON DAN 16
# #! Object Oriented Programming (OOP)
# # model object je npr konobar a attributi - su varijable a metode su stvai koj mogu da radi - funkcije
# # Turtle je module i ovde imas celu dokumentaciju kako radi
# # https://docs.python.org/3/library/turtle.html
# # Ovaj ispod link je link za sve boje koje se nalaze u Turtle
# # https://cs111.wellesley.edu/reference/colors

# # klasa se pise velikim prvim slovima reci

# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen

# # Trutle sa velikim t je klasa
# ori = Turtle() # --> blueprint
# ori.shape("turtle") # --> oblik kakav hocemo da nam ima 
# ori.color("darkolivegreen") # --> biras boju za blueprint
# print(ori)

# ori.forward(100) # --> pomerice se za 100 napred


# #! Object attributes
# my_screen = Screen()

# #!canvheight je attribut
# print(my_screen.canvheight) # --> atribut za visinu

# #!metoda je
# my_screen.exitonclick() # --> exit on click

#Paketi sa bibljotekama za python
#https://pypi.org/
#https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
#https://pypi.org/project/prettytable/
#https://pokemondb.net/pokedex/game/x-y

# da bi koristili morate da instalirate prvo python -m pip install -U prettytable

# uvozimo sada klasu
from prettytable import PrettyTable

#proba
x = PrettyTable()
# #* jedno po jedan row
# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# x.add_row(["Adelaide", 1295, 1158259, 600.5])
# x.add_row(["Brisbane", 5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])
# 
# print(x)
# #*mnogo row odjednom
# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# x.add_rows(
#     [
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],
#     ]
# )
# print(x)

# #*kolone
# x.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
# x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
# print(x)


#koristeci dokumentaciju pravim tabelu
table = PrettyTable()
# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachy", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])
# print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electirc", "Water", "Fire"])
print(table)

#sada atribute menjamo da bude centrirana levo

print(table.align)
table.align = "l"
print(table)

#! KVIZ
# 1 - Question 1:
# In OOP what is the name of the blueprint for creating objects?
# Class

# 2 - Question 2:
# Given a Class blueprint for a Car has the following attributes and methods, which line of code in the answers will produce an error?
# Attributes:
# num_of_seats
# speed
# Methods:
# drive()
# brake()

# car.drive() ok je za method
# car.num_of_seats = 2 ok je za atribute
##### car.brake() = 0 brake is a method, which means it's a function associated with the car object. We cannot assign a value to a function call.
# print(car.speed) ok je za atribute da printa 

# 3 - Question 3:
# my_toyota = Car()
# my_fiat = Car()
# What word would you use to describe what's inside my_toyota and my_fiat?
# my_toyota je variables
# Correct! my_toyota and my_fiat are variables and each contains a Car object.
# Object



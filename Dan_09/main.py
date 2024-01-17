#PYTHON DAN 9
#! Dictionaries and Nesting 

# Dictionaris imaju key i value
# Pišu se sa {key: value}
student = {"ime": "Aleksa Vlku"}
# Ako imam više key onda ih odvajajam sa , 
podaci_student = {
    "name": "Ankica",
    "age": 27,
    "city": "Novi Sad"
}

#! primer dictionary sa vise unosa
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", # --> gledaj da ih odmah formatiras 
    "Function": "A piece of code that you can easily call over and over again.", # --> uvek stavljaj , i na poslednji jer ako nekada budeš dodavao naknadno stvari
    "Loop": "The action of doing something over and over again", 
}

#! pozivanje elemnta prema key
print(programming_dictionary["Bug"]) # --> posto je u ovom slucaju key string pise se sa ""
print(programming_dictionary["Function"])
print(programming_dictionary["Loop"]) # --> da je pisalo smao Loop onda bi se smatralo da je Loop varijabla ali je nigde nismo definisali (npr. Loop = "neka vrednost koja ce se dodeliti varijabli loop")

#! ako pozivas nesto sto nije u dictionary dobices KeyError

#! dodavanje itema u dictionary
# napises samo novi key u [] i onda mu dodelis vrednost (value), vodis racuna o tipu podatka string, integer
programming_dictionary["Profesionalac"] = "To je definicija Aleksa za pola godine :)."
print(programming_dictionary) # --> {'Bug': 'An error in a program that prevents the program from running as expected.', 'Function': 'A piece of code that you can easily call over and over again.', 'Loop': 'The action of doing something over and over again', 'Profesionalac': 'To je definicija Aleksa za pola godine :).'}

#! pravljenje praznog dictionary
# nekada je vrlo korisno na pocetku da se napravi prazan dictionary
empty_dictionary = {} # --> prazna lista se slicno ovako pisala samo sa [] zagradama

#! brisanje postojeceg dictionary
#programming_dictionary = {}
#print(programming_dictionary) # --> obrisemo sve postojece iteme iz dictionary, korisno na primer ako se prati skor u igrici i na kraju igrice se on obrise

#! Editovanje itema u dictionary
programming_dictionary["Bug"] = "Kada Leka nesto zabrlja"
print(programming_dictionary["Bug"])

#! Loop kroz dictionary
# ovako ce svaki key da prinatuje
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]) # --> ovako printuje value
# ovako ce svaki value da prinuje
for value in programming_dictionary.values():
    print(value)
# ovako ce svaki key isto da printuje    
for key in programming_dictionary.keys():
    print(key)
# ovako se printuju celi itemi pojedinacno    
for item in programming_dictionary.items():
    print(item)    

#! 1 - VEŽBA
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.
# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for student_name in student_scores:
  if student_scores[student_name] >= 91 :
     student_grades[student_name] = "Outstanding" 
  elif 81 <= student_scores[student_name] <= 90 :
     student_grades[student_name] = "Exceeds Expectations"
  elif 71 <= student_scores[student_name] <= 80 :
     student_grades[student_name] = "Acceptable"   
  elif student_scores[student_name] <= 70 :
     student_grades[student_name] = "Fail"   

# 🚨 Don't change the code below 👇
print(student_grades)

#! Nesting list and dictionaries
#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists
travel_log = [
    {
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12,
    },
    {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5,
    },
]

#! 2 - VEŽBA
#You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.
#Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.
#add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
#DO NOT modify the travel_log directly. The goal is to create a function that modifies it.
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(name, times_visited, cities_visited): # --> namerno nazovi parametre drugacije od vrednosti 
    new_dic = {}
    new_dic['country'] = name
    new_dic['visits'] = times_visited
    new_dic['cities'] = cities_visited
    #dodavanje novog dictionary
    travel_log.append(new_dic)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

#! KVIZ
#? 1 - kako se dolazi do final_dictionary
startin_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
startin_dictionary["c"] = 7
final_dictionary = startin_dictionary
print(final_dictionary)

#? 2 - koja linija koda ce biti sa greskom
# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# dict["c"] = [1, 2, 3] # --> ovo moze

# print(dict[1]) # --> ovo ne moze jer nema [] indeksa u dictionary

#? 3 - koja linija koda ce printati "Steak"
order = {
   "starter": {1: "Salad", 2: "Soup"},
   "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
   "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2]) # --> ovo printa listu ['Steak']

print(order["main"][2][0]) # --> ovo printa konkretno index 0 u listi tj. Steak

#! FINALE Secret Auction Program
# The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually. 
# ```
# Welcome to the secret auction program. 
# What is your name?: Angela
# ```
# ```
# What's your bid?: $123
# ```
# ```
# Are there any other bidders? Type 'yes' or 'no'.
# yes

# ```
# If there are other bidders, the screen should clear, so you can pass your phone to the next person. If there are no more bidders, then the program should display the name of the winner and their winning bid. 

# ```
# The winner is Elon with a bid of $55000000000
# ```

import os
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
dalje = True

ucesnici = {}
najveca_suma = 0
pobednil = ""


def secret_auction(ime_aukcionara, ulog):
    ucesnici[ime_aukcionara] = ulog

while dalje:
    ime = input("# Welcome to the secret auction program. What is your name?:\n")
    bid = input("# What's your bid?:\n$")
    secret_auction(ime, bid)
    pitanje = input("Are there any other bidders? Type 'yes' or 'no'.")
    if pitanje != "yes":
        for key in ucesnici:
            if int(ucesnici[key]) > int(najveca_suma):
                najveca_suma = ucesnici[key]
                pobednik = key
        print(f"Pobednik aukcije je {pobednik} sa ponuđenom sumom od {najveca_suma}$")
        dalje = False
    else:
        os.system('cls')
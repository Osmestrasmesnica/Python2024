 #! PYTHON DAN 26

#! List and Dictionary Comprehension

#! List Comprehension

#* Stvaranje nove liste pomocu stare npr. sa for peltjom
numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n=1
    new_list.append(add_1)

#* Stvaranje nove liste pomocu Liste Comprehension
#! new_list = [new_item for item in list]
numbers = [1,2,3]
new_list_comprehension = [n+1 for n in numbers]
print(new_list_comprehension)

#* Moze da se koristi i na string
name = "Ankica voli Leku"
new_list_string = [slovo for slovo in name]
print(new_list_string)

#* Sequences in python su ove dole, i karakteristika im je da sve imaju neki odredjen redosled (specific order)
# list
# range
# string
# tuple

#* Upotreba range sa list comprehension:
raspon = range(1,5) # --> 1,2,3,4
new_list_raspon = [broj*2 for broj in raspon]
print(new_list_raspon)

#* Conditional List Comprehension - dodatno postoji neki uslov koji mora da se ispuni da bi se nova lista stvorila
#! new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [ime for ime in names if len(ime) < 6]
print(short_names)

#TODO Napraviti listu sa svim velikim slovima
upper_case_list = [ime.upper() for ime in names if len(ime) > 5]
print(upper_case_list)

#! ZADACI

#TODO You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.
# e.g. 4 * 4 = 16
# 4 squared equals 16.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number*number for number in numbers]
print(squared_numbers)

#TODO In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.
# First, use list comprehension to convert the list_of_strings to a list of integers.
# Then use list comprehension again to create a new list called result. This new list should only contain the even numbers from the list numbers.
# Example Input
# 9, 0, 32, 8, 2, 8, 64, 29, 42, 99
# Example Output
# [0, 32, 8, 2, 8, 64, 42]
#### FALI INPUT OVDE
# list_of_strings = input().split(',')
# list_of_integers = [int(item) for item in list_of_strings]
# result = [number for number in list_of_integers if number%2 == 0] 
# print(result)

#TODO Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

# You are going to create a list called result which contains the numbers that are common in both files.
# e.g. if file1.txt contained:
# 1
# 2
# 3
# and file2.txt contained:
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT: The output should be a list of integers and not strings! Try to use List Comprehension instead of a Loop.
# Example Output
# [3, 6, 5, 33, 12, 7, 42, 13]

with open("Dan_26/file1.txt") as file:
  data = file.readlines()
  new_list1 = [int(number.strip()) for number in data if number.strip().isdigit()]

with open("Dan_26/file2.txt") as file:
  data = file.readlines()
  new_list2 = [int(number.strip()) for number in data if number.strip().isdigit()]

result = [number for number in new_list1 if number in new_list2] # --> za svaki broj iz(prvo in) liste 1 proveriti da lise broj nalazi u (drugo in) listi 2

# Write your code above 👆
print(result)


#! Dictionary Comprehension

# Mozemo da pravimo nov dictionary potpuno
#! new_dict = {new_key:new_value for item in list}

# Mozemo da napravimo vec na osnovu postojeceg dictionary
#! new_dict = {new_key:new_value for {key,value} in dict.items()}

# Mozemo i uslov na kraju da dodamo
#! new_dict = {new_key:new_value for {key,value} in dict.items() if test}

# Hocemo da dobijemo
# students_scores = {
#    "Aleksa":100,
#    "Ankica":100,
#    "Caroline": 97,
#     ...
# }

import random

imena = ['Aleksa', "Ankica", "Caroline", "Dave", "Eleanor", "Freddie", "John Doe"]
students_scores = {student:random.randint(1,100) for student in imena}
print(students_scores)

#! Loop through dictionaries
#! new_dict = {new_key:new_value for {key,value} in dict.items() if test}
passed_students = {student:score for student,score in students_scores.items() if score > 51}
print(passed_students)

#TODO You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
#Try Googling to find out how to convert a sentence into a list of words. 
# koristi se .split()
sentence = "Teško je leteti sa orlovima kada radiš sa ćurkama. :)"
list_of_words = sentence.split()
result = {word:len(word) for word in list_of_words}

print(result)

#TODO You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f use this formula:
# (temp_c * 9/5) + 32 = temp_f
# The eval() function will help us convert the string input into a Python dictionary, provided that the inputs are already formatted with the correct syntax.

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temperature * 9/5) + 32 for day,temperature in weather_c.items()}
print(weather_f)

#! LOOPS WITH PANDAS
import pandas

student_dict = {
   "student": ["Angela", "James", "Lily"],
   "scores": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#    print(key, value)

#! Looping through DataFrames - rows of a data frame
students_data_frame = pandas.DataFrame(student_dict)
print(students_data_frame)

#!for (index, row) in DataFrame.iterrows():
for (index, row) in students_data_frame.iterrows():
  #  print(row)
  #  print(row.student)
  #  print(row.scores)
   if row.student == "James":
    print(row.scores)

#! Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
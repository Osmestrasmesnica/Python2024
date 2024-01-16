#PYTHON DAN 5
# Python loops
#! FOR LOOP U LISTAMA
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie") # --> ovo je unutar petlje tako da se izvrsava onoliko puta koliko ima fruit odnosno elemenata u listi
print(fruit) # --> ovo je van for loop, tako da se izvrsava nakon izvrsene petlje 

#! 1- VEŽBA
# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Input a Python list of student heights
print("Unesite visine studenata kao na primer: 153 135 175 205....")
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sumaVisine = 0
brojStudenata = 0
for i in student_heights :
  sumaVisine += i
  brojStudenata += 1

print(f"total height = {sumaVisine}")
print(f"number of students = {brojStudenata}")
print(f"average height = {round(sumaVisine/brojStudenata)}") # --> koristimo round a ne integer!!!

#! 2- VEŽBA
#You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
# The highest score in the class is: x
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
#! Aleksaino resenje ali se nije trazilo ovako
#print(sorted(student_scores))
sortirano = sorted(student_scores)
print(f"The highest score in the class is: {sortirano.pop()}")
#! Kurs resenje
highest_score = 0
for score in student_scores :
    if score > highest_score :
        highest_score = score

print(f"The highest score in the class is: {highest_score}")


#! FOR LOOP VAN PETLJI sa in range()
# range() funkicja for number in range(a, b): uraditi nesto...
# range(1, 10) odradice funkciju od 1 do 9 ali nece i 10 da obuhvati isto... ako hocemo i 10 onda u zagradi pisime (1, 11)
# range(1, 11, 3) ova 3 znaci da ce uraditi nesto tek za svaki 3 broju nizu
for number in range(1,10): # --> od 1 do 9 printa
    print(number)
for number in range(1,11): # --> od 1 do 10 printa
    print(number)
for number in range(1,11,3): # --> svaki 3 ce da printa 1, 4, 7, 10
    print(number)

#suma prvih 100 brojeva
total = 0
for broj in range(0, 101): # --> koristimo 101 zato sto hocemo sumu prvih 100 brojeva
    total += broj
print(total)

#! 3- VEŽBA
# You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
# Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
suma = 0
for broj in range(0, target + 1, 2): # --> dodajemo targe + 1 da ako je unet paran broj racuna i njega kao poslednjeg a ako je unet neparan broj svakako ga nece obuhvatit
  suma += broj
print(suma)

#! RESENJE KURSA
even_sum = 0
for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)

# or

alternative_sum = 0
for number in range(1, target + 1):
  if number % 2 == 0:
    alternative_sum += number
print(alternative_sum)

#! 4- VEŽBA
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# Write your code here 👇
target = 100
for i in range(1, target+1,):
  if i % 15 == 0 : # --> prvo se printa ovo sto je najvece  inace bi za 15, 30 i ... printao prvo Fizz, ili Buzz, zavisi sta je napisano prvo u if petlji
    print("FizzBuzz")
  elif i % 3 == 0 :
      print("Fizz")
  elif i % 5 == 0 :
    print("Buzz")
  else:
    print(i)

#! FINALE ZA DANAS - PASSWORD GENERATOR
#! ********************************************************************
#! VERZIJA ALEKSA
# The program will ask:
# How many letters would you like in your password?
# How many symbols would you like?
# How many numbers would you like?    
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []
for letter in range(1, nr_letters + 1): # --> mora + 1 da bi obuhvatio i broj koji smo mi zadali 
  password.append(random.choice(letters)) # --> random.choice() da se dobiju pojedinacni elementi iz liste
for number in range(1, nr_numbers + 1):
  password.append(random.choice(numbers)) # --> random.choice() da se dobiju pojedinacni elementi iz liste
  #password += random.chochoice(numbers) # --> moze i ovako da se pise
for symbol in range(1, nr_symbols + 1):
  password.append(random.choice(symbols)) # --> random.choice() da se dobiju pojedinacni elementi iz liste
  #password += random.chochoice(symbols) # --> moze i ovako da se pise
#print(password)
password_join = ''.join(password) 
print(password_join)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(password) # --> random.shuffle() mesanje elemenata u listi
password_join = ''.join(password) # --> da se spoje svi elementi u string, '' ovde je sta ce biti izmedju svakoga, u ovom slcaju nista, ',' u ovom slucaju , 
print(f"Vaša šifra je: {password_join}")

#! VERZIJA SA KURSA
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters)) # --> moze ovako a mozes i sa += 

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
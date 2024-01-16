#PYTHON DAN 8
#! Function parameters and Caesar Cipher parameters
#! FUNKCIJE
# Definisanje funkcije
def my_function(): # -->  function
    print("this is my function")
    #Do this
    #Then do this
    #Finally do this
my_function() # --> calling function

# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# Simple function
def greet():
    print("Srce")
    print("Srca")
    print("Stoooooo")
greet()

# Function that allows for input
# 'name' is the parameter.
# 'Aleksa i Ankica' is the argument.
# Parametar  -- name(something) naziv podataka koji se unosi u funkciju
# Argument -- Aleksa(123) sama vrednost podatka koji se unosi u funkciju
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Aleksa i Ankica")

# Functions with more than 1 input
# Oba parametra se unose i razdvajaju se zarezom
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")
greet_with("Aleksa Vlku", "Donja Pilica")

# Calling greet_with() with Positional Arguments
# U suštini bitan je redosled kojim se parametri unose, uvek će biti kao parametri
greet_with("Aleksa Vlku", "Majdanpek") # --> Hello Aleksa Vlku, WHat is it like in Majdanpek
#vs.
greet_with("Majdanpek", "Aleksa Vlku") # --> Hello Majdanpek, WHat is it like in Aleksa Vlku

# Calling greet_with() with Keyword Arguments
# Ali ako daš parametrima odmah argumente onda možeš da ih unosiš kako hoćeš, odnosno nije onda više bitan redosled
greet_with(location="London", name="Angela")

#! VEŽBA 1
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height x wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 \* 4) / 5
# number of cans = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
# Write your code below this line 👇
import math # --> modul da možeš da koristiš math.celi koji zaokružuje na prvi najveći broj od toga koj ti imaš
def paint_calc(height,width,cover):
  number_of_cans = (height * width) / cover
  cans = math.ceil(number_of_cans) # --> returns the smallest integer higher or equal to x
  print(f"You'll need {cans} cans of paint.")
# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#! VEŽBA 2
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# Write your code below this line 👇
#? LEKINO RESENJE
def prime_checker(number):
  if number % 2 != 0 and number % 3 != 0 and number % 5 != 0:
    print("It's a prime number.")
  elif number == 3 or number == 5 or number == 2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

#? RESENJE NA KURSU
def prime_checker1(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
        is_prime = False
    if is_prime:
       print("It's a prime number.")
    else:
       print("It's not a prime number.")    
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)

#! Caesar Cipher Code
# part 1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
def encrypt(plain_text, shift_amount):
    print(text)
    print(shift)
    encripted_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > 25:
            new_position -= 26
        encripted_text += alphabet[new_position]
    print(f"Skrivena poruka je : {encripted_text}")
encrypt(plain_text=text, shift_amount=shift)
    

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# part 2
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    #e.g.
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"
    original_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if new_position < 0:
            new_position += 26
            original_text += alphabet[new_position]
        else:
            original_text += alphabet[new_position]
    print(f"The decoded text is {original_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print('Niste uneli "encode" ili "decode"')

# part 3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(start_text, shift_amount, cipher_direction):
    cipher_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_amount
            if new_position > 25:
                new_position -= 26
            cipher_text += alphabet[new_position]
        elif cipher_direction == "decode":
            new_position = position - shift_amount
            if new_position < 0:
                new_position +=26
            cipher_text += alphabet[new_position]
        else:
            print("Neispravno uneta komanda")
    print(f"The {cipher_direction}d text is {cipher_text}")
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# part 4

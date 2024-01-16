#PYTHON DAN 7
#! Flow Chart
# Bitno je da koristis Flow Chart da predočiš sebi logiku pre nego što počneš da radiš
# Meni je konkretno uvek lakše da ja to nacrtam sebi na papiru/tabli ali možeš i da koristiš ovaj sajt
# https://app.diagrams.net/

#!Pyton liste koje možeš da koristiš
# https://developers.google.com/edu/python/lists#for-and-in

#! FINALE ZA DANAS - HANGMAN
#! ********************************************************************
#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#?Verzija - Aleksa
#list_lenght = len(word_list) # --> ovo je integer ako si zaboravio
#list_indexes = list_lenght - 1
#index_random_reci = random.randint(0,list_indexes) # --> random integer od 0 do duzina niza-1 i tako se dobiju indeksi
#chosen_word = word_list[index_random_reci]
#print(chosen_word)

#? Verzija - KURS
chosen_word = random.choice(word_list) # --> elegantniji nacin da se izabere random iz liste

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Unesite ispod slovo koje zelite da proverite:\n ").lower() # --> lower() funkcija za smanjivanje slova

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#?Verzija - Aleksa -- ja sam samo proveravao da li se nalazi ili ne
# if guess in chosen_word :
#     print(f"Vaše slovo '{guess}' se nalazi u reči {chosen_word}.")
# else:
#     print(f"Vaše slovo '{guess}' se ne nalazi u reči {chosen_word}")

#? Verzija - KURS -- ovde svako slovo u reci se proverava... ovo je bolje
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

#Step 2
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
display2 = []
for slovo in chosen_word:
    display.append("_")
    # display += "_" moze i ovako
print(display)

guess = input("Guess a letter: ").lower()

guess_length = len(guess) # --> da vidimo koliko je dugacka rec

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#?VERZIJA - ALEKSA -- verzija sa novom listom
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#         display2.append(letter)  # --> ako je slovo kao iz reci onda appendujemo to slovo
#     else:
#         print("Wrong")
#         display2.append("_") # --> ako nije to slovo onda dodajemo samo _
# print(display2)

#?VERZIJA - KURS -- verzija sa starom listom

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
    else:
        display[position] = "_"

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)

#Step 3
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

#Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You won!")

#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")
while not end_of_game:
    starting_number_of_blanks = display.count("_")
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #? aleksina verzija koja radi ali duzi je kod
    # if display.count("_") == starting_number_of_blanks:
    #     starting_number_of_blanks -= 1
    #     lives -= 1
    #     print(f"Izabrano slovo {guess} se ne nalazi u reči. Izgubili ste jedan zivot.")
    #     print(lives)

    #? jednostavnije je bilo
    if guess not in chosen_word:
        lives -= 1
        print(f"Izabrano slovo {guess} se ne nalazi u reči. Izgubili ste jedan zivot.")
        print(lives)
        if lives == 0:
            end_of_game = True
            print("Izgubili ste.")
            
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    #? aleksina verzija koja radi ali je duzi kod
    # if lives == 0:
    #     end_of_game = True
    #     print("Izgubili ste.")
        
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

#Step 5

import random
import os
from hangman_words import word_list
from hangman_art import logo, stages

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')


#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"Nažalost izabrano slovo {guess} nije u reči. Izgubili ste jedan zivot.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])


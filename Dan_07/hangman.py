import random
import os
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Nažalost izabrano slovo {guess} nije u reči. Izgubili ste jedan zivot.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Izgubili ste.")
            print(f'Pssst, the solution is {chosen_word}.')

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("Pobedili ste.")

    print(stages[lives])


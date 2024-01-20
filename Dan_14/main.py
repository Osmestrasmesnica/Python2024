#PYTHON DAN 14
# Ko ima vise pratilaca na instagramu 
from art import logo, vs
from game_data import data
import random
import os

guess1 = random.choice(data)
score = 0
game_over = False    

print(logo)

def display_score(score):
    print(f"Vas skor je {score}")

def display_celebrity(celebrity):
    return f"{celebrity['name']}, {celebrity['description']} from {celebrity['country']}"

#while
while not game_over:
    guess2 = random.choice(data)
    print(f'Compare A: {display_celebrity(guess1)}')
    print(vs)
    print(f'Against B: {display_celebrity(guess2)}')
    print("Who has more follower on instagram? Type 'A' or 'B':")
    followers_choice = input().lower()
    if guess2 == guess1:
        guess2 = random.choice(data)
    if followers_choice == "a":
        if guess1["follower_count"] > guess2["follower_count"]:
            os.system("cls")
            print(logo)
            print("####################################################")
            print(f'{guess1["name"]} has more followers on instagram! {guess1["name"]} has {guess1["follower_count"]} mil. followers on instagram vs {guess2["name"]} who has {guess2["follower_count"]} mil. followers on instagram.')
            score += 1
            display_score(score)
            print("####################################################")
            guess1 = guess2
        elif guess1["follower_count"] < guess2["follower_count"] or guess1["follower_count"] == guess2["follower_count"]:
            os.system("cls")
            print(logo)
            print("####################################################")
            print(f'{guess1["name"]} has {guess1["follower_count"]} mil. followers on instagram and {guess2["name"]} has {guess2["follower_count"]} mil. followers on instagram.')
            print("Izgubili ste! :(")
            display_score(score)
            game_over = True
    elif followers_choice == "b":
        if guess2["follower_count"] > guess1["follower_count"]:
            os.system("cls")
            print(logo)
            print("####################################################")
            print(f'{guess2["name"]} has more followers on instagram! {guess2["name"]} has {guess2["follower_count"]} mil. followers on instagram vs {guess1["name"]} who has {guess1["follower_count"]} mil. followers on instagram.')
            score += 1
            display_score(score)
            print("####################################################")
            guess1 = guess2
        elif guess2["follower_count"] < guess1["follower_count"] or guess2["follower_count"] == guess1["follower_count"]:
            os.system("cls")
            print(logo)
            print(f'{guess2["name"]} has {guess2["follower_count"]} mil. followers on instagram and {guess1["name"]} has {guess1["follower_count"]} mil. followers on instagram.')
            print("Izgubili ste! :(")
            display_score(score)
            game_over = True
    else:
        os.system("cls")
        print(logo)
        print("Unesite ispravne komandae sledeći put...")
        display_score(score)
        game_over = True


#! RAZMISLI O OVOJ FUNKCIJI
# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"
        
# #proveravamo da li smo pogodili ko ima vise followera
# is_correct = check_answer(guess, a_follower_count, b_follower_count)

# os.system('cls')
# print(logo)
# if is_correct:
#     score += 1
#     print(f"You're right! Current score: {score}.")
# else:
#     game_should_continue = False
#     print(f"Sorry, that's wrong. Final score: {score}")
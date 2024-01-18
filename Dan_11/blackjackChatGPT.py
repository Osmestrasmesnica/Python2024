import random

def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculate and return the total score of a list of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, computer_score):
    """Compare the scores and determine the winner."""
    if player_score > 21 and computer_score > 21:
        return "You went over. You lose!"
    if player_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has Blackjack. You lose!"
    elif player_score == 0:
        return "You have Blackjack. You win!"
    elif player_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Blackjack!")

    player_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]

    is_game_over = False

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass: ")
            if should_continue == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

# Start the game
play_game()

from art import tictactoe
from functions import display_board, replace_value, more_turns, reset_board, check_winner, continue_playing, ai_move, play_game

def main():
    """Main function to start the game."""
    print(tictactoe)
    players = input(f"Koliko playera igra ovu igru? Unesi broj (1/2)... ")
    koigraprvi = input("Da li želite da igrate prvi (X) ili drugi (O). Unesite (x/o)...")

    play_game(players, koigraprvi)

if __name__ == "__main__":
    main()
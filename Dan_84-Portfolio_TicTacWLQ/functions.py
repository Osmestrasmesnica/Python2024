import os
import random

def display_board(board):
    """Display the game board."""
    print("-"*30)
    print("Izgled trenutne table")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i != len(board)-1:
            print("-" * 9)

def replace_value(board, current_symbol, counter, koigraprvi):
    """Find a value in the updated board and replace it with the current player symbol."""
    try:
        value = input("Enter the number where you want to place your symbol: ")
        if value not in [str(num) for num in range(1, 10)]:
            print("Molimo vas unesite broj između 1 i 9.")
            return False

        counter = counter % 2
        symbol = current_symbol[counter]

        for row_idx, row in enumerate(board):
            for col_idx, cell in enumerate(row):
                if cell == value:
                    board[row_idx][col_idx] = symbol
                    os.system('cls')
                    display_board(board)
                    return

        print("Već postoji unos na ovom mestu..")
        return False
    except ValueError as e:
        print("Molimo vas unesite broj, a ne slovo ili znak.")
        return False

def more_turns(board):
    """Check if all numbers are replaced in board."""
    for row in board:
        for cell in row:
            if cell.isdigit():
                return False
    return True

def reset_board():
    """Reset the game board."""
    return [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

def check_winner(board):
    """Check if there is a winner."""
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    return None

def continue_playing():
    """Ask the player if they want to continue playing."""
    play_again = input("Da li želite da igrate ponovo? (da/ne): ")
    return play_again.lower() == "da"

def ai_move(board, symbol):
    """Generate AI's move."""
    available_positions = [(row_idx, col_idx) for row_idx, row in enumerate(board) for col_idx, cell in enumerate(row) if cell.isdigit()]
    row, col = random.choice(available_positions)
    position = board[row][col]
    board[row][col] = symbol
    os.system('cls')
    display_board(board)
    return position

def choose_symbol():
    """Choose the symbol to play with."""
    symbol = input("Da li želite da igrate kao 'X' ili 'O'? (x/o): ").lower()
    while symbol not in ['x', 'o']:
        symbol = input("Molimo vas odaberite 'X' ili 'O': ").lower()
    return symbol

def play_game(players, koigraprvi):
    """Play the Tic Tac Toe game."""
    while True:
        board = reset_board()
        current_symbol = ["X", "O"]
        play_on = True
        counter = 0

        display_board(board)

        if players == '1':
            human_symbol = current_symbol[0] if koigraprvi.lower() == 'x' else current_symbol[1]
            ai_symbol = current_symbol[0] if human_symbol == current_symbol[1] else current_symbol[1]

            while play_on:
                if (counter % 2 == 0 and koigraprvi.lower() == 'x') or (counter % 2 == 1 and koigraprvi.lower() == 'o'):
                    position = replace_value(board, current_symbol, counter, koigraprvi)
                else:
                    position = ai_move(board, ai_symbol)
                    print(f"AI plays at position {position}")

                counter += 1

                winner = check_winner(board)
                if winner:
                    print(f"IGRAČ {winner} JE POBEDIO!")
                    break
                elif more_turns(board):
                    print("IT IS A TIE")
                    break
        elif players == '2':
            while play_on:
                replace_value(board, current_symbol, counter, koigraprvi)
                counter += 1

                winner = check_winner(board)
                if winner:
                    print(f"IGRAČ {winner} JE POBEDIO!")
                    break
                elif more_turns(board):
                    print("IT IS A TIE")
                    break
        else:
            print("Unesite ispravan broj igrača (1 ili 2).")

        if not continue_playing():
            break
        koigraprvi = choose_symbol()

from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z', 'ć', 'č', 'ž', 'š', 'đ' 
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
    print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)

ponovno_pokretanje = True
while ponovno_pokretanje:
    direction = input("Upišite 'encode' da šifrujete poruku ili upišite 'decode' da je dešifrujete:\n")
    text = input("Upišite Vašu poruku:\n").lower()
    shift = int(input("Upišite tajni broj za šifrovanje:\n"))

    if shift > 31:
        shift = shift % 31
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
   
    ponovno = input(
        "Da lu želite da opet koristite naš program 'EnigmaExpress'? Upišite 'da' ako želite još jednom da probate ili 'ne' ukoliko to ne želite.\n"
    ).lower()
    if ponovno == "ne":
        ponovno_pokretanje = False
        print("Hvala vam na na koriscenju.")

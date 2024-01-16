import os
from art import logo

print(logo)
dalje = True

ucesnici = {}

pobednil = ""


def secret_auction(ime_aukcionara, ulog):
    ucesnici[ime_aukcionara] = ulog

def winner_auction(bidding_record_dict):
    najveca_suma = 0
    for key in bidding_record_dict:
        if int(bidding_record_dict[key]) > int(najveca_suma):
            najveca_suma = bidding_record_dict[key]
            pobednik = key
    print(f"Pobednik aukcije je {pobednik} sa ponuđenom sumom od {najveca_suma}$")
    print(ucesnici.items())

while dalje:
    ime = input("# Welcome to the secret auction program. What is your name?:\n")
    bid = input("# What's your bid?:\n$")
    secret_auction(ime, bid)
    pitanje = input("Are there any other bidders? Type 'yes' or 'no'.")
    if pitanje != "yes":
        winner_auction(ucesnici)
        dalje = False
    else:
        os.system('cls')
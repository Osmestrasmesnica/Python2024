# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("Dan_26/nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# new_dict = {row["letter"]:row["code"] for index, row in df.iterrows()}
# print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print("Unesite neko ime i ja ću Vama da napišem kako se ono čita koristeći NATO ALPHABET...")
unos = input().upper() #! obavezno pretvoriti u upper jer su sva slova u dict upper

#TODO 3. Create a function that takes a word and returns a list of the phonetic code words for that word.
nato_phonetic_alphabet = [new_dict[slovo] for slovo in unos if slovo in new_dict]

print(nato_phonetic_alphabet)
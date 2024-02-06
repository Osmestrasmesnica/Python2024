# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#! Update project 
#TODO Nesto sto nije u dict izbaciti error
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as error_msg:
        print(f"Unesite samo slova koja se nalaze u alphabetu. Uneli ste: {error_msg} a to se ne nalazi u alphabetu")
        generate_phonetic()
    print(output_list)

generate_phonetic()
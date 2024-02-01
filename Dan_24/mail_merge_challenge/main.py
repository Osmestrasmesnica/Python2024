 #TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# ucitava svaku liniju teksta kao listu
#! readlines() 

#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# menjas prvi string, sa drugim stringom
#! replace()

#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# brises razmake pri i posle stringa
#! strip()
PLACEHOLDER = "[name]"

with open("Dan_24/mail_merge_challenge/Input/Names/invited_names.txt") as imena:
        list_with_names = imena.readlines()

with open("Dan_24/mail_merge_challenge/Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for ime in list_with_names:
        bez_razmaka = ime.strip()
        new_letter = letter_content.replace(PLACEHOLDER, bez_razmaka)
        with open(f"Dan_24/mail_merge_challenge/Output/ReadyToSend/{bez_razmaka}_pozivnica.txt", mode="w") as nov_fajl:
            nov_fajl.write(new_letter)
            print(nov_fajl)
    
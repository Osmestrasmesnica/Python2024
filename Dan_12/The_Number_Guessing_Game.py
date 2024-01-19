from art import logo
import random
import os

def check_guess(pokusaj, random_broj, zivot):
    if pokusaj == random_broj:
        if pokusaj == 1:
            print(f"BRAVOOOOOO... TRENUTNO JE U LEKINOJ GLAVI {random_broj} ANKICA")
        elif pokusaj < 5:
            print(f"BRAVOOOOOO... TRENUTNO JE U LEKINOJ GLAVI {random_broj} ANKE")
        else:
            print(f"BRAVOOOOOO... TRENUTNO JE U LEKINOJ GLAVI {random_broj} ANKI")
        return False, zivot
    elif pokusaj > random_broj:
        print("Broj je ipak malo nizi")
        print("Probajte ponovo")
        zivot -= 1
    elif pokusaj < random_broj:
        print("Broj je ipak malo visi")
        print("Probajte ponovo")
        zivot -= 1
    
    return True, zivot

print(logo)
print("****************")
print("Dobrodošli u Pogodi Broja Ankica koje se nalaze u Lekinoj glavi")
print('''Leka ima trenutno u glavi mnogo Ankini... Kao na primer: \n'Mogu'l te nešto zamolit?", "Sce scaaa stoo", "Inami?! INAMI?!" "A jel me voliš? A Što?"...itd''')
print("Ako želite samo malo da se igrate 'ljube', a ukoliko ste spremni za izazov 'inami'")
unos = input().lower()
os.system('cls')

nije_pogodila = True

if unos == "ljube":
    zivot = 10
    random_broj = random.randint(1, 101)
    print(random_broj)
    while nije_pogodila and zivot > 0:
        print(f"Imate {zivot} pokusaja")
        print("Trenutno je Leki u glavi xxx broj Anki? Pogodi koliko je to? Unesite broj od 1 do 100:")
        pokusaj = int(input())
        nije_pogodila, zivot = check_guess(pokusaj, random_broj, zivot)

    if zivot == 0 and nije_pogodila:
        print(f"Žao nam je, niste pogodili. Tačan broj je bio {random_broj}.")

elif unos == 'inami':
    zivot = 5
    random_broj = random.randint(1, 101)
    print(random_broj)

    while nije_pogodila and zivot > 0:
        print(f"Imate {zivot} pokusaja")
        print("Trenutno je Leki u glavi xxx broj Anki? Pogodi koliko je to? Unesite broj od 1 do 100:")
        pokusaj = int(input())
        nije_pogodila, zivot = check_guess(pokusaj, random_broj, zivot)

    if zivot == 0 and nije_pogodila:
        print(f"Žao nam je, niste pogodili. Tačan broj je bio {random_broj}.")

else:
    print("Niste uneli dobar unos. Probajte ponovo da startujete i pratite lepo uputstva....")

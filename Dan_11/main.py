from art import logo, city
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

nastavi_dalje = True

# dobrodošlica
print("Dobrodošli u kuću strave. Da li želite da igrate Blackjack / 21 sa nama? Upišite 'da' ili 'ne':")

# igraš ili ne
početak_igre = input().lower()

# funkcija za deljenje karata
def deljenje(špil):
    karte_PC = random.choices(špil, k=2)          
    karte_Player = random.choices(špil, k=2)
    return karte_PC, karte_Player

# funkcija za još jednu kartu
def hit(špil):
    dodatna_karta = random.choice(špil)
    return provera_11(dodatna_karta, sum_PC, sum_Player)

# provera 11
def provera_11(karta, sum1, sum2):
    return 1 if karta == 11 and (karta + sum1 > 21 or karta + sum2 > 21) else karta

while nastavi_dalje:
    if početak_igre == "ne":
        os.system('cls')
        print('****************************************************************')
        print("Očigledno ste došli samo da razgledate. Uživajte dalje u pogledu...bedo bedna")
        print(city)
        print('****************************************************************')
    else:
        os.system('cls')
        print('****************************************************************')
        print(logo)
        print('****************************************************************')
        karte_PC, karte_Player = deljenje(cards)
        prva_karta_PC = karte_PC[0]
        sum_PC = sum(karte_PC)
        sum_Player = sum(karte_Player)
        print(f"Vukove karte su: {prva_karta_PC} i 'x' ... ******ovo obrisati kasnije {karte_PC}")
        print(f"Vaše karte su: {' i '.join(map(str, karte_Player))}, suma je : {sum_Player}")
        print('****************************************************************')
        print('****************************************************************')
        print('****************************************************************')
        print("Da li želite da vučete kartu ili ste zadovoljni sa trenutnom sumom? Ako hoćete da vučete napište 'da', a ako ste zadovoljni 'ne'")
        vuci = input("")
        if vuci == "ne":
            # Ako je PC izvuko ispod 17, po pravilima mora da vuče još jedu kartu
            while sum_PC < 17:
                dodatna_karta = hit(cards)
                sum_PC += dodatna_karta
                karte_PC.append(dodatna_karta)
                print(sum_PC, karte_PC)
            if sum_PC > 21:
                print(f"Pobedili ste. Kompjuterov zbir je {sum_PC} a vaš je {sum_Player}")
            elif sum_PC == sum_Player:
                print(f"Nereseno je. Vuk ima {karte_PC} a Vi {karte_Player} a suma Vam je ista {sum_PC}.")
            elif sum_PC < sum_Player:
                print(f"Pobedili ste. Kompjuterov zbir je {sum_PC} a vaš je {sum_Player}")    
            else:
                print(f"Izgubili ste. Kompjuterov zbir je {sum_PC} sa kartama {karte_PC} a vaš je zbir {sum_Player} sa kartama {karte_Player}")
        
        elif vuci == "da":
            vuci_opet = True
            while vuci_opet:
                print('****************************************************************')
                print('****************************************************************')
                print('****************************************************************')
                dodatna_karta = hit(cards)
                sum_Player += dodatna_karta
                karte_Player.append(dodatna_karta)
                if sum_Player > 21:
                    print(f"Vaše karte su: {' i '.join(map(str, karte_Player))}, suma je : {sum_Player}")
                    vuci_opet = False
                    opet_vuci = 'ne'
                else:    
                    print(f"Vaše karte su: {' i '.join(map(str, karte_Player))}, suma je : {sum_Player}")
                    print("Da li zelite opet da vucete kartu? Upisite 'da' ako zelite ili 'ne' ako ne zelite")
                    opet_vuci = input("").lower()
                if opet_vuci != "da":
                    vuci_opet = False

            while sum_PC < 17:
                dodatna_karta = hit(cards)
                sum_PC += dodatna_karta
                karte_PC.append(dodatna_karta)
                print(sum_PC, karte_PC)
            
            if sum_Player > 21:
                print(f"Izgubili ste. Vaš zbir je {sum_Player} sa kartama {karte_Player} i prošli ste preko 21")
            elif sum_PC > 21:
                print(f"Pobedili ste. Vuk se malo zaneo. Suma Vukovih karata je {sum_PC} sa kartama {karte_PC} i premšio je broj 21")
                print(f"Vaše karte su: {karte_Player},a Vaša suma je : {sum_Player}")
            elif sum_PC == sum_Player:
                print(f"Nereseno je. Vuk ima {karte_PC} a Vi {karte_Player} a suma Vam je ista {sum_PC}. Moraćete da naučite da delite bratski")
            elif sum_PC > sum_Player:
                print(f"Izgubili ste. Kompjuterov zbir je {sum_PC} sa kartama {karte_PC} a vaš je zbir {sum_Player} sa kartama {karte_Player}")
            else:
                print(f"Pobedili ste. Kompjuterov zbir je {sum_PC} a vaš je {sum_Player}")                
        else:
            print("Unesite ispravnu komandu sledeći put. Sada morate sve ispočetka jer ne znate da pratite uputstva...:)")
    print("Da li želiš opet da igraš? Upiši 'da' ako želiš i 'ne' ako ne želiš.")
    pitanje_za_dalje = input().lower()
    if pitanje_za_dalje == "ne":
        nastavi_dalje = False
        os.system('cls')
        print('****************************************************************')
        print("Hvala sto ste igrali Blackjack")

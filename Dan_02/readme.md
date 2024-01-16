Dan02 - Tipovi podataka i matematičke operacije

1 - Postoje 4 tipa podataka:
    1 - String tip - stoje pod "", tekst, brojevi...
    2 - Integer tip - celi brojevi
    3 - Float tip - decimalni brojevi, . i , menjamo _ kod velikih brojeva
    4 - Boolean tip - ima samo 2 forme, True i False

2 - Funkcija za proveru tipa podatka 
    type()

3 - Funkcije za promenu tipa podatka su:
    str()
    int()
    boolean()
    float()

4 - Kada izvlačiš iz stringa karakter na nekom mestu stavljaš [], i brojanje kreće od 0

5 - Matematičke operacija u Pythonu
Rezultati matematičkih operacija su uvek u format tipu float
Ako ima više operacija u redu PEMDASLR --> redosled je (), **, * i /, + i -, od leva na desno
    sabiranje 3 + 5, 
    oduzimanje 7 - 3, 
    množenje 3 * 2, 
    deljenje 6 / 3 --> rezultat je ovde 2.0
    stepenovanje 2 ** 3
    deljenje gde se dobije ineger odnosno samo ceo broj bez ostatka 8 // 3 --> 2
    samo ostatak 9 % 4 --> 1

6 - Koristimo funkciju round(float type, broj decimala) da zaokruzimo broj na nekoliko decimala
    print(8/3) # --> 2.666666
    print(int(8/3)) # --> 2
    print(round(8/3)) # --> 3
    print(round(8/3,2)) # --> 2.67

7 - Matematičke operacije na već postojeću varijablu bez ponavljanja koda
    +=, -=, /=, *=

8 - Krošćenje f-stringa u Pythonu gde dodajemo pre fukncije f, a integer ili bilo koji drugi format koji zelimo da ubacimo koristimo {} zagrade
    print(f"Nešto ovde piše i sada pominjem neki broj koji iznosi {broj}")

9 - Zaokruživanje na 2 decimale iako je posle toga 0 npr. 12.60 (umesto 12.6 koji se dobiju ukoliko koristimo funkciju round())
    "{:.2f}".format(varijabla)
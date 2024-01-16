Dan04 - RANDOMIZATION AND LISTS
RANDOMIZATION
1 - Kada imamo neke module i hocemo da ih koristimo, onda moramo da ih importujemo na pocetku. Module mozes i sam da pravis i da ih importujemo iz drugih foldera
    import naziv_modula

2 - koristimo random. da generisemo random neke stvari
    random.random() # -> ovo je module za stvaranje random broja izmedju 0 i 1 ali ne ukljucuje 1
    random.randint(x, y) #--> u ovom slučaju stvaramo random integer (cele brojeve), u zagradi je raspon uključujući i te brojeve

3 - random decimalni brojevi od 0 do 5 ali ne i 5
    random.random() * 5 # --> mnozimo sa tim brojem do koga zelimo

LISTE
4 - liste se pišu sa [] zagradama, i unutra mogu biti svi tipovi podatak i string i integer i ostali... 
    fruits = ["Jabuka", "Jagoda", "Kruska"]

5 - redosled u listi je redosled kojim je dodavano, odnosno sa leva na desno, od starijeg ka mladjem/novijem

6 - liste krecu od broja 0, a ne od broja 1

7 - ako hocemo da print neki konretan item u nizu, npr hocemo da printamo koji je 3. item u nizu onda koirstimo [2], opet koristimo [] zagrade
    item[2]
8 - moze se koristiti i negativan broj [-1] i to je poslednji item u nizu

9 - ako hocemo da menjamo item u nizu, biramo koji je u nizu [] 
    lista[2] = "kako_hocemo_da_menjamo"

10 - ako hocemo da dodamo nesto novo na niz koirsimo funkciju .append
    list.append("stahocemodaunesemo")

11 - pored ove funkcije mozemo jos da koristimo .extend () dodaje svaki elemnt liste u vec postojecu listu kao pojedinacne listove, za razliku od appenda koji bi dodao elemnte sve zajedno kao jednu listu, .insert(i, x) i je indeks itema pre koga zelimo da ubacimo nov item, x je sta zelimo da unesemo, .remove(x) brisanje prvog elementa sa ovim vrednostima iz liste, .clear() sve elemente brise iz liste, .count(x) broji koliko puta se x ponavlja u listi, sort(*, key=None, reverse=False) za sortiranje... 
    states_of_america = ["Delaware", "Pennsylvania"]
    states_of_america[1]= "Majdanpek" # --> hocemo da zamenimo na drugoj poziciji sta je bilo sa ovim sto ovde sada pisemo
    states_of_america.append("Bor") # --> dodali smo na niz "Bor"

SUŠTINA JE DA NE PAMTIŠ SVE OVE FUNKCIJE VEĆ DA PROČITAŠ DOKUMENTACIJU I DA AKO ZNAŠ DA JE NEŠTO MOGUĆE DA TO PRONAĐEŠ NA NETU U DOKUMENTACIJI

12 - funkcija .split() koja splits the string into individual elements and puts them inside a List, u zagradi su ono čime ih odvajaš
    names = names_string.split(", ") --> u ovom slucaju odvajamo ih zarezom i razmakom

13 - Error koji se pojavljuje ako iskoristis len() i posle toga uzmes to kao index npr... lista[len()] jer ce len uzeti od 1 do i a lista ide od 0 do i... tj index je len() - 1
    IndexError

14 - NestedList spajanje dve ili vise lista, i ima [] [] onoliko koliko ima lista
    voće =["jagoda", "nektarina", "jabuka", "grožđe", "breskva", "višnja", "kruška"]
    povrće = ["spanać", "kelj", "paradajz", "celer", "krompir"]
    prljavi_plodovi = [voće, povrće] # --> [["jagoda", "nektarina", "jabuka", "grožđe", "breskva", "višnja", "kruška"], ["spanać", "kelj", "paradajz", "celer", "krompir"]]





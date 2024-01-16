Dan03 - Conditioning

1 - IF/ELSE uslovi, uvek moraju da su u istoj ravni if i else, a uslov se piše pre :
    if x > 0 :
        print ("Leka je kralj")
    else :
        print ("Leka nije kralj")

2 - Operacije za IF/ELSE
    >, <, <=, >=, == (jednako), != (nije jednako)

3 - Kada koristimo jedan = onda dodeljujemo neku vrednost nekoj varijabli a kada koristimo dva == onda proveravamo da li je varijabla jednaka nekoj vrednosti
    height = 200 # --> sada je vrednost 200 
    height == 200 # --> proverava se da li je vrednost 200
    
4 - Nested (ugneždene) IF/ELSE statement
    if condition : # --> prvo se ovo proverava i ako je dobro izvršavaju se akcije unutar ovoga
        if another condition: # --> pa se ovo proverava
            do this # --> ovo se izvršava ako je iznad ovo dobro
        else:   # --> ako iznad nije dobro onda se ovo izvršava
            do this
    else: # --> ako je prvobitan if condition netacan onda se ovo izvršava
        do this

5 - Ako imamo više conditioninga (uslova) onda koristimo
    ELIF

    if condition1:
        do A
    elif condition2:
        do B
    else:
        do this

6 - Ako ima više IF statement koje želimo da se odrade onda gledamo da su oni u istom redu (da je isti "indentation")

7 - ELSE ne mora da se piše ako ne radiš ništa dalje sa varijablom

8 - Logical operators
    and --> kada treba da su oba uslova ispunjena
    or --> kada jedan ili drugi uslov moraju da su ispunjeni
    not --> kada uslov nije ispunjen

9 - funkcije
    lower() --> pretvara sve u mala slova
    count() --> koliko se puta ponavalja u stringu to sto je u zagradi

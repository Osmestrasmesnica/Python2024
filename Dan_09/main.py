#PYTHON DAN 9
# Dictionaries and Nesting 

# Dictionaris imaju key i value
# Pišu se sa {key: value}
student = {"ime": "Aleksa Vlku"}
# Ako imam više key onda ih odvajajam sa , 
podaci_student = {
    "name": "Ankica",
    "age": 27,
    "city": "Novi Sad"
}

#! primer dictionary sa vise unosa
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", # --> gledaj da ih odmah formatiras 
    "Function": "A piece of code that you can easily call over and over again.", # --> uvek stavljaj , i na poslednji jer ako nekada budeš dodavao naknadno stvari
    "Loop": "The action of doing something over and over again", 
}

#! pozivanje elemnta prema key
print(programming_dictionary["Bug"]) # --> posto je u ovom slucaju key string pise se sa ""
print(programming_dictionary["Function"])
print(programming_dictionary["Loop"]) # --> da je pisalo smao Loop onda bi se smatralo da je Loop varijabla ali je nigde nismo definisali (npr. Loop = "neka vrednost koja ce se dodeliti varijabli loop")

#! ako pozivas nesto sto nije u dictionary dobices KeyError

#! dodavanje itema u dictionary
# napises samo novi key u [] i onda mu dodelis vrednost (value), vodis racuna o tipu podatka string, integer
programming_dictionary["Profesionalac"] = "To je definicija Aleksa za pola godine :)."
print(programming_dictionary) # --> {'Bug': 'An error in a program that prevents the program from running as expected.', 'Function': 'A piece of code that you can easily call over and over again.', 'Loop': 'The action of doing something over and over again', 'Profesionalac': 'To je definicija Aleksa za pola godine :).'}

#! pravljenje praznog dictionary
# nekada je vrlo korisno na pocetku da se napravi prazan dictionary
empty_dictionary = {} # --> prazna lista se slicno ovako pisala samo sa [] zagradama

#! brisanje postojeceg dictionary
#programming_dictionary = {}
#print(programming_dictionary) # --> obrisemo sve postojece iteme iz dictionary, korisno na primer ako se prati skor u igrici i na kraju igrice se on obrise

#! Editovanje itema u dictionary
programming_dictionary["Bug"] = "Kada Leka nesto zabrlja"
print(programming_dictionary["Bug"])

#! Loop kroz dictionary
# ovako ce svaki key da prinatuje
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]) # --> ovako printuje value
# ovako ce svaki value da prinuje
for value in programming_dictionary.values():
    print(value)
# ovako ce svaki key isto da printuje    
for key in programming_dictionary.keys():
    print(key)
# ovako se printuju celi itemi pojedinacno    
for item in programming_dictionary.items():
    print(item)    

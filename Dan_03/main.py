#PYTHON DAN 3
# CONDITIONING if/else statements

#! IF/ELSE statements
# Koristi se neki uslov i : nakon toga šta se dešava ako je uslov ispunjen
# Voditi računa da su if i else u istoj ravni a da se sve sto se desava u okviru njih mora pisti uvučeno
# Operacije za IF/ELSE >, <, <=, >=, == (jednako), != (nije jednako)
# Kada koristimo jedan = onda dodeljujemo neku vrednost nekoj varijabli a kada koristimo dva == onda proveravamo da li je varijabla jednaka nekoj vrednosti
visina = int(input("Dobrodošli. Da li želite postanete najpoznatiji patuljak na svetu?\nPostanite član udruženja patuljaka, počnite kao pomagač Deda Mrazu a završite u okršaju sa Legolasom!\nPotrebna nam je samo Vaša visine u centrimetrima.\nDakle, koliko ste niski?\n"))
if visina >= 120 :
    print("Previsoki ste da se učlanite u klub patuljaka. Možda ipak da pogledate poziciju koja zahteva težinu, na primer mesto Deda Mraza...")
else : 
    print("Dobrodošao u klub patuljaka")

#! 1 - VEŽBA
# Write a program that works out whether if a given number is an odd or even number.
# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
ostatak = number % 2
if ostatak == 0 : # --> ako nema ostatka onda je broj paran
  print("This is an even number.")
else : # --> ako ima ostatka onda je broj neparan
  print("This is an odd number.")

#! Nested IF/ELSE statements
# Obratiti pažnju samo kojim redosledom se ovde izvršavaju radnje, da ide prvo prvi IF ako je dobar onda se sve u okviru njega radi dalje ako nije dobar odmah se ide na njegov ELSE
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120 :
  print ("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 12 :
    print ("Please pay $5.")
  else :
    print ("Pleas pay $7.")
else :
  print ("Sorry, you have to grow taller before you can ride.")

#! Ako imamo više uslova onda koristimo ELIF
# ako prvi uslov nije ispunjen a imamo još uslova onda koristimo ELIF
print("Dobrodošli na rolerkoste!")
height = int(input("Koliko ste visoki u centimetrima? "))

if height >= 120 :
  print ("Možete da se vozite, samo potpišite ugovor ovde!")
  godine = int(input("Koliko imate godina? "))
  if godine <= 12 :
    print ("Platite $5.")
  elif 12 < godine < 18 :
    print ("Platite $7.")
  else :
    print ("Platite $10.")
else :
  print ("Izvinjavam se, ali DA LI JE OVO NORMALNO?! Izvinite što se derem, ali da li ste normalni? ")

#! 2 - VEŽBA
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.

visina = float(input("Unesite vašu visinu u metrima npr. 1.72 / 1.86"))

težina = float(input("Unesite vašu težinu u kilogramima npr. 72 / 86"))

bmi = visina / (težina ** 2)

if bmi < 18.5 :
  print(f"Vaš BMI je {bmi} i Vi ste neuhranjeni, potražite pomoć")
elif 18.5 <= bmi < 25 :
  print(f"Vaš BMI je {bmi} i Vi ste idealne težine, svaka čast")
elif 25 <= bmi < 30 :
  print(f"Vaš BMI je {bmi} i Vi ste blago gojazni, malo vam fali ali na vama je da odlučite ka kojoj granici")
elif 30 <= bmi < 35 :
  print(f"Vaš BMI je {bmi} i Vi ste debeli")
else :
  print(f"Vaš BMI je {bmi} i Vi ste klinički gojazni, potražite pomoć")

#! 3 - VEŽBA
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.
# This is how you work out whether if a particular year is a leap year.
# on every year that is divisible by 4 with no remainder
# except every year that is evenly divisible by 100 with no remainder
# unless the year is also divisible by 400 with no remainder
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if year % 4 == 0 :
  if year % 100 == 0 :
    if year % 400 == 0 :
      print("Leap year")
    else:
      print("Not leap year")  
  else:
    print("Leap year")  
else:
  print("Not leap year")

#! Multiple IF statements
# Bitno je samo da su svi unutar istog "indentation" ako želimo više if statement da koristimo
# Ne zaboraviti na početku da stavimo varijablu bill (račun) na 0
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 # --> ne zaboraviti ovaj deo da se doda

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3 # --> dodavanje na inicajlni bill koji se nalaz u okviru ovog if statementa
  print(f"Your final bill is ${bill}") # --> ne mora else da se piše očigledno, zato što u else ne bi ništa radili sa bill varijablom onda ne moramo ni da pišemo ništa

else:
  print("Sorry, you have to grow taller before you can ride.")

#! 4 - VEŽBA
# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1  
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
račun = 0
if size == "S" :
  račun +=15
  if add_pepperoni == "Y" :
    račun +=2 
elif size == "M" :
  račun +=20
  if add_pepperoni == "Y" :
    račun +=3
elif size == "L" :
  račun +=25
  if add_pepperoni == "Y" :
    račun +=3

if extra_cheese == "Y" :
  račun +=1
print(f"Your final bill is: ${račun}.")

#! Logical operators
a = 12 #  --> postavljanje varijable
a > 10 #  --> True
a < 10 #  --> False
a > 10 and a < 15 #  --> True, kada se koristi AND oba moraju uslova da su ispunjena da bude True
a > 10 and a > 15 # --> False
a > 10 or a > 15 #  --> True, kada je OR barem jedno mora uslov da se ispunjava
not a > 15 #  --> True, kada se koristi NOT onda se negira to sto je u uslovu, tj obrnuto od onoga sto je u uslovu se dobija

#ako su ljudi u krizi srednjih godina (između 45 i 55 godina) karta za rolerkoster neka im je besplatna
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 # --> ne zaboraviti ovaj deo da se doda

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55 :
    bill = 0 # --> ovaj deo može potpuno da se izbaci zato što će se preskočiti ceo deo gde ima modifikacija računa, tako da ne mora ni da stoji ovo ovde
    print("Midlife crysis tickets are $0.")
  else :
    bill = 12
    print("Adult tickets are $12.")
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3 # --> dodavanje na inicajlni bill koji se nalaz u okviru ovog if statementa
  print(f"Your final bill is ${bill}") # --> ne mora else da se piše očigledno, zato što u else ne bi ništa radili sa bill varijablom onda ne moramo ni da pišemo ništa

else:
  print("Sorry, you have to grow taller before you can ride.")

#! 5 - VEŽBA
#LOVE CALCULATOR
#Na osnovu koliko se puta pominju neka slova računamo koliki je LOVE SCORE
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is *z*."
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# Check if either name1 or name2 matches the specified names
if name1.lower() == "aleksa vlku" or name1.lower() == "ankica milovanovic" or \
   name2.lower() == "aleksa vlku" or name2.lower() == "ankica milovanovic":
    print("Ma vi ste kliknuli ∞∞∞, becane moooooj, SCE SCA STOOOOOOOOO")
else:
    # Combine the names and convert to lowercase
    both_names = (name1 + name2).lower()

    # Count occurrences of letters
    T = both_names.count("t")  # --> ovde dobijamo integer koliko se puta to sto je u zagradi ponavlja u stringu
    R = both_names.count("r")
    U = both_names.count("u")
    E = both_names.count("e")
    L = both_names.count("l")
    O = both_names.count("o")
    V = both_names.count("v")
    E = both_names.count("e")

    # Calculate the love score
    first_digit = T + R + U + E
    second_digit = L + O + V + E
    zbir = int(str(first_digit) + str(second_digit)) # --> da bi se dobio broj sa dve cifre od integera, pretvaramo ga u string pa opet u integer jer ga koristimo posle za >, < uslove

    if zbir >= 90 or zbir <= 10:
        print(f"Your score is {zbir}, you go together like coke and mentos. Ove veze su za snimanje i pratnju")
    elif 40 <= zbir <= 50:
        print(f"Your score is {zbir}, you are alright together. Ma OK ste....")
    else:
        print(f"Your score is {zbir}. Verovatno i u horoskop veruejte")

#! FINALE ZA DANAS - CHOOSE YOUR ADVENTURE
#! ********************************************************************
#! VERZIJA 1
        
print('''
*********************************************
     anka       ,@@@@@@@,        leka
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
wlq \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_ori
*********************************************
''')

print("Dobrodošli u Ankicinu avanturu.")
print("Vaša misija je da pronađete blago...odnosno ALEKSU.\n") 


print("Ankice....Probudila si se u začaranoj šumi. Ispred tebe su dva puta, koji ćeš odabrati?")

print("1. Idi osvetljenim putem sa šarenim orhidejama i zelenim mahovinama.")

print("2. Idi mračnim, misterioznim putem.")

choice1 = input("Izaberi 1 ili 2: ")

if choice1 == "1":
    print("********************************************************************************************************************************")
    print("\n\nBravo, vidi se da si dosta horora gleda. Izabrala si put sa šarenim orhidejama i sa mahovinama i naišla si na magičnu žabu.")
    print("Žaba ti je ponudila da ti pokaže dalje put kroz šumu.")
    print('''
     ______
    (__  __)
      |  |
      |  |________........--------........________                  __
      |  |\\                                      ~~~~~~~~------~~~~  ||
      |  | \\                             o                           ||
      |  |  ||                         o^/|\^o                        ||
      |  |  ||                     o\*`'.\|/.'`*/o                    ||
      |  |  ||                      \\\\\\|//////                     ||
      |  |  ||                       {><><@><><}                      ||
      |  |  ||                       ).--._.--.(                      ||
      |  |  ||                       ( O     O )                      ||
      |  |  ||:::::::::::::::::      /   . .   \       :::::::::::::::||
      |  |  ||:::::::::::::::::     .`._______.'.      :::::::::::::::||
      |  |  ||:::::::::::::::::    /(    \_/    )\     :::::::::::::::||
      |  |  ||:::::::::::::::::: _/  \  \   /  /  \_ :::::::::::::::::||
      |  |  ||::::::::::::::::::::::::::::::::::::::::::::::::::::::::||
      |  |  ||::::::::::::::::::::::::::::::::::::::::::::::::::::::::||
      |  |  ||::::::::::::::::::::::::::::::::::::::::::::::::::::::::||
      |  |  ||::::::::::::::::::::::::::::::::::::::::::::::::::::::::||
      |  |//::::::''""''""''""''~~~~~~~~'""'""''""''""''::::::::::::::~~
      |  |                                         ~~~~~~~~~~
      |  |                       THE MAGIČNA ŽABA
 ''')
    

    print("1. Prihvataš da pratiš magičnu žabu kroz čarobnu šumu.")
    print("2. Ljubazno odbijaš da kreneš sa žabom kroz šumu i nastavljaš sama u suprotnom smeru.")

    choice2 = input("Izaberi (1 ili 2): ")

    if choice2 == "1":
        print("********************************************************************************************************************************") 
        print("\n\nŽaba te vodi do mističnog magičnog portala.")
        print("Prolaskom kroz portal, našla si se u drugom univerzumu.")
        print('''
 8                            8
 8      /```|     .@@@@@,     8
 8     |  66|_    @@@@@@@@,   8 (\/)
 8     C     _)   aa`@@@@@@   8  \/
 8(\/)  \ ._|    (_   ?@@@@   8
|8:\/:~:~) /:~:~: =' @@@@~:~:~8
|8::::::/\\/`\;_:::\ (__::::::8
|8:::::| \ '|___/` \\// `\):::8
|8::::|| | '|::/ /  ^^  \ \:::8
|8::::|| | ' \:| \__/\__/ |:::8
|8o:::|\ \  ' |:\_\    /_/::::8o
|"8o:::=\ \===::/`\`%%`/'\::::"8o
|\"8o~|  \_\  \|   `""`   |:~:~\8o
\ \"8o\   )))  \           \::::"8o
 \ \"8o\`.  \   \           \::::"8o
  \|~~~~~| -|| -|mmmmmmmmmmmm~~~~~|
   `~~~~~|  ||  |~~|  |~|  |~~~~~~
         |  ||  |  |__| |__|
         |  ||  |  \  | \  |
         |__||__|  (~~^\(~~^\/
         (   \   \  `-._)`-._)
          `-._)-._)
          LEKA     ∞∞∞     ANKA
''')
        print("Ankica pronalazi Aleksu, oni kliknu i žive srećno do kraja života. Oboje ste pobedili!∞∞∞ BRAVO ANKAAAAA ∞∞∞")

    elif choice2 == "2":
        print("********************************************************************************************************************************")
        print("\n\nRazdrala si suviše glasno STRAŠNA ŽABA.")
        print('''
                      __ --~~--_     _--~~--__
                   _-~         \---/         ~-_
                 /~     __--~~\     /~~--__     ~\.
                /   _-~~       |   |       ~~-_   \.
               |  /~            | |            ~\  |
               | /      O       | |       O      \ |
               | |             |   |             | |
                \ \_         _/     \_         _/ \.
                 ~-_~--___--~  b   d  ~--___--~_-~
                  / ~~---    _________    ---~~ \.
                  / ~~---    _________    ---~~ \.
                 /  __---~~~~         ~~~~---__  \.
                _-~~                           ~~-_
              /~                                   ~\/
            (_-~                                 ~-_)
               \                                   \/
              _-~-_                             _-~-_
            /     ~~--___               ___--~~     \/
           /             ~~~~-------~~~~             \/
           |                                         |
          |                                           |
      _  |                                           | _
   _-~ ~-|      /                            \      |-~ ~-_
  /      |     |                              |     |      \/
 (       |    |                                |    |       )
  \     ~-|   |                                |   |-~     \/
   ~-_     |   |                              |   |     _-~
        ~-_   \   \                            /   /   _-~
           ~-_/    )                          (    \_-~
           _-~    (~-_                      _-~)    ~-_
         (    _     \  ~~--___   _-_   __--~~  /     _  )
         _-~       ~-_   )  ~~~   ~~~  (  _-~     ~-_
        (   _-~/ |\   )--~~           ~~--(   /| \~-_  )
               ( |  ~-~                     ~-~  | )
''')
        print("Nažalost, žaba te je čula i nije imala smisla za humor. Stigla te je i pojela. Nisi pronašla LEKU")
        print("GAME OVER")

elif choice1 == "2":
    print("********************************************************************************************************************************")
    print("\n\nOčigledno ništa nisi naučila iz horor filmova i odabrala si ovaj jezivi mračni put.")
    print("Dok se upuštate dublje u tamu, čujete čudne zvuke.")
    print('''
       /\.
      /  \.--./\.
     /    \  /  \.
    /      \/    \ .       .--.
   /     |\_/|    \       |   | .---.
  /     / o o\     \      |   | |   | .---.
 /      /(   )\     \     |   `-'   |_|   |
/       / \#/ \      \    |         ._____'
        |     |           `---.     |
        | | | |                |    |
      (~\ | | /~)              |    |
     __\_|| ||_/__             |    |
___///_//_| |_\\__\\\__________|____|
''')

    print("1. Nastavi da hodaš. Ne...Nastavi da trčiš...trči brže...KAŽEM BRŽEEEEEEE.")
    print("2. Okreni se nazad da vidiš šta se to čuje.")

    choice3 = input("Izaberi (1 ili 2): ")

    if choice3 == "1":
        print("********************************************************************************************************************************")
        print("\n\nNailazite na prijateljsko stvorenje zvano ORI i ono ti pomaže da se snađeš na ovoj tamnoj stazi.")
        print('''
        ..
         $. ,o$$$o.
         $. $$$$$$$o.   ..
        .$. $' $$$$$$ ,o''
       .$'  $  '$$$$$,o'.,'   .oo'
      .$'   $.   $$$$'  ,,  .o'.
     .$'    '$o. 'O$ ..ooo'',oo'
    .$'     .o$'  '$$''     ,,o'
  .%$,,,,,ooO'      '      ,,o''
.$o.          ,o'   $o    ..oo'
 ''O,,,,,,,,,'      $'$. .o'
    '$        $       '$,'o' '
    '$        $      .o $
     '$       $       .$$
      '$      $,     .o$$
       '$     $.    ,o' $
        $.    '$.   $,oooo''o,
        $.     $.  'o'       '$
        $.     $.     .,ooo,  $
      .''      'oo...o'  $ 'o $
                      $  $   ''
                      $  $
                      $  %
                     ,$  $
                     $  $'
                      ''
''')
        print("Nakon nekog vremena, dolazite do LEKE i spašavate ga dotadašnje dosade koju je ima bez VAS.∞∞∞ BRAVO ANČIKICEEEEEE !!∞∞∞ VOLI TE LEKA")

    elif choice3 == "2":
        print("********************************************************************************************************************************")
        print('''
                                                      ,--,  ,.-.
                        ,                   \,       '-,-`,'-.' | ._
                       /|           \    ,   |\         }  )/  / `-,',
                       [ '          |\  /|   | |        /  \|  |/`  ,`
                       | |       ,.`  `,` `, | |  _,...(   (      _',
                       \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\.
                        \  \_\,``,   ` , ,  /  |         )         _,/.
                         \  '  `  ,_ _`_,-,<._.<        /         /.
                          ', `>.,`  `  `   ,., |_      |         /.
                            \/`  `,   `   ,`  | /__,.-`    _,   `\.
                        -,-..\  _  \  `  /  ,  / `._) _,-\`       \.
                         \_,,.) /\    ` /  / ) (-,, ``    ,        |
                        ,` )  | \_\       '-`  |  `(               \.
                       /  /```(   , --, ,' \   |`<`    ,            |
                      /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
                ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
               (-, \           ) \ ('_.-._)/ /,`    /.
               | /  `          `/ \\ V   V, /`     /.
            ,--\(        ,     <_/`\\     ||      /.
           (   ,``-     \/|         \-A.A-`|     /.
          ,>,_ )_,..(    )\          -,,_-`  _--`
         (_ \|`   _,/_  /  \_            ,--`
          \( `   <.,../`     `-.._   _,-`
           `                      ```
        ''')
        print("\n\nOkrenula si se. ZAŠTO?...očigledno nisi dovoljno horora gleda.... zna se ko sve prvi umire....STRAŠNOOOOO LJUBEEEE")
        print("Šuma je počela da menja oblik")
        print("Izgubila si se i nikada nisi pronašla Aleksu. Game over!")

else:
    print("********************************************************************************************************************************")
    print("Nepravilan unos.. Da li znaš da pratiš uputstva? Da li si ikada sklapala policu od IKEA-e???. Game over.")

#! VERZIJA 2
#! OVO JE VERZIJA UZ CHAT GPT
import time

# Definisanje inventara
inventory = []

def show_ascii_art(art):
    """
    Prikazuje određeni ASCII art.
    """
    print(art)

def start_game():
    """
    Početak igre - uvodna priča.
    """
    print("Dobrodošli u Ankicinu avanturu.")
    print("Vaša misija je da pronađete blago...odnosno ALEKSU.\n")

def choose_path():
    """
    Biranje puta na početku igre.
    """
    print("Ankice....Probudila si se u začaranoj šumi. Ispred tebe su četiri puta, koji ćeš odabrati?")
    print("1. Idi osvetljenim putem sa šarenim orhidejama i zelenim mahovinama.")
    print("2. Idi mračnim, misterioznim putem.")
    print("3. Idi kroz tunel sa svetlima.")
    print("4. Kreni putem sa visećim mostom.")
    return input("Izaberi 1, 2, 3 ili 4: ")

def path_1():
    """
    Potezi kada se odabere prvi put.
    """
    print("\n\nBravo, vidi se da si dosta horora gledala. Izabrala si put sa šarenim orhidejama i mahovinama i naišla si na magičnu žabu.")
    print("Žaba ti je ponudila da ti pokaže dalje put kroz šumu.")
    
    print("1. Prihvataš da pratiš magičnu žabu kroz čarobnu šumu.")
    print("2. Ljubazno odbijaš da kreneš sa žabom kroz šumu i nastavljaš sama u suprotnom smeru.")
    return input("Izaberi (1 ili 2): ")

def path_1_choice_1():
    """
    Potezi nakon što se prihvati put sa magičnom žabom.
    """
    print("\n\nŽaba te vodi do mističnog magičnog portala.")
    print("Prolaskom kroz portal, našla si se u drugom univerzumu.")
    print("Ankica pronalazi Aleksu, oni kliknu i žive srećno do kraja života. Oboje ste pobedili!∞∞∞ BRAVO ANKAAAAA ∞∞∞")

def path_1_choice_2():
    """
    Potezi nakon što se odbije pratiti magičnu žabu.
    """
    print("\n\nNažalost, žaba te je čula i nije imala smisla za humor. Stigla te je i pojela. Nisi pronašla LEKU")
    print("GAME OVER")

def path_2():
    """
    Potezi kada se odabere drugi put.
    """
    print("\n\nOčigledno ništa nisi naučila iz horor filmova i odabrala si ovaj jezivi mračni put.")
    print("Dok se upuštate dublje u tamu, čujete čudne zvuke.")
    
    print("1. Nastavi da hodaš. Ne...Nastavi da trčiš...trči brže...KAŽEM BRŽEEEEEEE.")
    print("2. Okreni se nazad da vidiš šta se to čuje.")
    return input("Izaberi (1 ili 2): ")

def path_2_choice_1():
    """
    Potezi nakon što se odluči nastaviti hodati kroz mračni put.
    """
    print("\n\nNailazite na prijateljsko stvorenje zvano ORI i ono ti pomaže da se snađeš na ovoj tamnoj stazi.")
    print("\n\nNakon nekog vremena, dolazite do LEKE i spašavate ga od dosade koju ima bez VAS.∞∞∞ BRAVO ANČIKICEEEEEE !!∞∞∞ VOLI TE LEKA")

def path_2_choice_2():
    """
    Potezi nakon što se odluči okrenuti nazad.
    """
    print("\n\nOkrenula si se. ZAŠTO?...očigledno nisi dovoljno horora gleda.... zna se ko sve prvi umire....STRAŠNOOOOO LJUBEEEE")
    print("Šuma je počela da menja oblik.")
    print("Izgubila si se i nikada nisi pronašla Aleksu. Game over!")

def path_3():
    """
    Potezi kada se odabere treći put.
    """
    print("\n\nUlaziš u tunel sa svetlima. Osećaš bljesak svetlosti kako te obavija.")
    print("1. Nastavi kroz tunel.")
    print("2. Okreni se i istraži drugi deo šume.")
    return input("Izaberi (1 ili 2): ")

def path_3_choice_1():
    """
    Potezi nakon što se odluči nastaviti kroz tunel.
    """
    print("\n\nStižeš do kraja tunela i izlaziš na prelepu livadu.")
    print("Naišao si na stvorenje koje ti daruje čarobnu svetlost.")
    print("1. Zadrži svetlost za sebe.")
    print("2. Pokloni svetlost stvorenju.")
    return input("Izaberi (1 ili 2): ")

def path_3_choice_2():
    """
    Potezi nakon što se odluči istražiti drugi deo šume.
    """
    print("\n\nNažalost, šuma postaje sve tamnija i gubiš orijentaciju.")
    print("Izgubio si se i nikada nisi pronašao Aleksu. Game over!")

def path_4():
    """
    Potezi kada se odabere četvrti put.
    """
    print("\n\nKrećeš putem sa visećim mostom. Most se ljulja na vetru.")
    print("1. Pređi most pažljivo.")
    print("2. Potraži alternativni put oko mosta.")
    return input("Izaberi (1 ili 2): ")

def path_4_choice_1():
    """
    Potezi nakon što se odluči preći viseći most.
    """
    print("\n\nUspešno prelaziš most. Sada si bliže pronalaženju Aleksa.")
    print("Nastavi putem kroz šumu.")
    print("1. Ubrzaj korak.")
    print("2. Zadrži trenutak da pogledaš oko sebe.")
    return input("Izaberi (1 ili 2): ")

def path_4_choice_2():
    """
    Potezi nakon što se odluči potražiti alternativni put oko mosta.
    """
    print("\n\nNažalost, gubiš vreme tražeći alternativni put.")
    print("Šuma postaje još mračnija, a Aleksa nikada ne pronalaziš. Game over!")

def end_game():
    """
    Završetak igre.
    """
    print("********************************************************************************************************************************")
    print("Nepravilan unos.. Da li znaš da pratiš uputstva? Da li si ikada sklapala policu od IKEA-e???. Game over.")

# Glavna funkcija koja pokreće igru
def main():
    start_game()
    path_choice = choose_path()

    if path_choice == "1":
        choice_1 = path_1()

        if choice_1 == "1":
            path_1_choice_1()
        elif choice_1 == "2":
            path_1_choice_2()
        else:
            end_game()

    elif path_choice == "2":
        choice_2 = path_2()

        if choice_2 == "1":
            path_2_choice_1()
        elif choice_2 == "2":
            path_2_choice_2()
        else:
            end_game()

    elif path_choice == "3":
        choice_3 = path_3()

        if choice_3 == "1":
            choice_3_1 = path_3_choice_1()

            if choice_3_1 == "1":
                print("\n\nČuvanje svetlosti za sebe dovodi do otkrića tajnog prolaza kroz šumu.")
                print("Uspešno pronalaziš Aleksu! ∞∞∞ BRAVO ANKAAAAA ∞∞∞")

            elif choice_3_1 == "2":
                print("\n\nPoklanjanje svetlosti stvorenju čini ga tvojim saveznikom.")
                print("Sa savezničkim stvorenjem, pronalaziš Aleksu! ∞∞∞ BRAVO ANKAAAAA ∞∞∞")

            else:
                end_game()

        elif choice_3 == "2":
            path_3_choice_2()

        else:
            end_game()

    elif path_choice == "4":
        choice_4 = path_4()

        if choice_4 == "1":
            choice_4_1 = path_4_choice_1()

            if choice_4_1 == "1":
                print("\n\nBrzim korakom prolaziš kroz šumu i uspešno nalaziš Aleksu! ∞∞∞ BRAVO ANKAAAAA ∞∞∞")

            elif choice_4_1 == "2":
                print("\n\nZadržavanje trenutka pomaže ti da primetiš skriveni trag koji vodi do Aleksa.")
                print("Uspešno ga pronalaziš! ∞∞∞ BRAVO ANKAAAAA ∞∞∞")

            else:
                end_game()

        elif choice_4 == "2":
            path_4_choice_2()

        else:
            end_game()

    else:
        end_game()

# Pokretanje igre
main()

#! VERZIJA 3 -- Tresure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
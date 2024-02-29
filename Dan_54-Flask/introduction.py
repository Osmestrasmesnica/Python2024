#! DAN 54
#! PHYTON DECORATORS
    
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()

#! 1 - VEZBA
# koliko puta treba da napisem nesto da bi me anka pogledala ALOOO SRCEE EPOGLEDAJ ME VIDI KAKO SAM KUUUUL COOOL COLL ili COOL NAAAA LJUBWEEEE POGLEDAJ ME VEC JEDNOM STA NOSIS STU STOLICU NE ZNAM DALI LEPO PSEM ILI SAMO NAGADJAM DUGMICE KOJI LI JE PROCENNAT TACNO NAPISANIH RECI KOJE SAM SADA OVDE UKUCAO ko ce ga yznati ja samo pisem ja samo puuutujem sve manje ludujeeem sve vise nestooooooe ne znam ni sam sta sve ovo pisem dok gledam u tebe SCE MOJE SCVASTOOOOOO DA LI CES POGLEDATI OVO ILI CES SAMO DA ME ISKULIRAS JER IMAS KAO NESTO DA RADIS XD JA cu ovo da pisem sve dok ne izadjes aloo srce ne mogu vise da pisem ovooooo osrcoooooo drcaaneeee becasneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee a luuuuuuubeeeeeeeeee dodoji ljubeee zapravo mi se jedu palacinke ali mi zao da ih sada spremas tu kada vidim da ipmas posla.... doduse mogla si da se ponudis sudove da operes XD ahhahahahah sali mse opracu ih ja nema veye samo da zavrsim ovo jao imam osecajda brljam nonst op ove zz i yy akda pisem ne mogu vise bole me ruke koliko ovo kuccam bilo bi lepo dkada bise sada pojavila iz tog jebenog spajza hahaha hljube breee sad cu da te zovem .... LJUUBEEEE!! a ti kazes samo EEEE i ne izlazis pa da sam hteo da ti cujem samo glas ne bih te zvaooo samo da izvucem kofere kaze ona a j ja cu da ti ih izvucem kazem ja ali ona me kulira hjahahahah ne izlazi iz og spajza evo cujem je kako sada ona sama tamo buce jao luuupa u ovo doba opet glasno boeljda da odem da joj pomognem evo izvukla je veliki kofer haha hprilaziii gotov sam XDDDD ili neee samo me isklurala....uzela metlu i djubravnik hahahahahah i vratila se u spajz pa jebemuuuu ljube sto me tako kuliras jahahahhaha ajd dodji da procitas ovo nasmejace te nadam ... verovatno sam poceo ja sada da perem sudeove a ti i dalje lupas u tom spajzu AJDE DODJI LJUUUBE pravi puauz hahahha SRCE RADIM NEST OVIDIS SRCE RECI STA HOCES nista kazem ja... reci AJD DA CITAS kad zavrsim da citas ALI ZAVRSIO SAM pa sta da citam.... i ode anka opet tmao xD ZIVOTE MOJ..... E STA TI JE ZLATKO REKAO ZA USISIVAC???? JESI ZAVRSIO A BRE COVECE DA DODJEM DA CITAM?! ljutito me anka pita a ja nastavljam da pisem a ona nastavlja da radi i kulira hahahahahha egvogasi svetlo kao dize mali kofer i vraca ga nazar JEBEM TI KOLIKO STVARI IMA TAMO SAD SAM GVIRUNUO I VIDEO. KOLiko ce li joj trebati da ovo procita evo vraca biciklu i valjda NDAAM SE dolazi ovamo. SRCKOOOOO DODJIII BECAAAANEEE skontaj kkao brzo pisem ovo i kazi kako je kuul tastatuuuur i kako sam ja cool dok ovako kao brzo pisem sad cu kada krenes ka ovamo da se pravim da jos vise nesto kucam i kao da je bitno ima da krenem samo da kucam neka slova znaci da si dosla KAZES AJDE i gasis svetlo KCUAM asjhdasj dkasjiiefj iajsfkas[fgdsmaikafj odjao aavj]
# PRESLAYKOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO VOLIM TE KUL TI JE TASTATURA STO MENJA BOJE, JA SAAD IDEM DA SE PAKUJEM, MORAM DA P[AKUJEM ZIMSKE STVARI I DA IH NOSIMO U PILICI DOK PISEM OVO RAZMISLJAM KAKO CEMO SUTRA ODNBETI STVARI U AUTO SRCEEEEEEEEEE ON MENI KAYE MMMMM JEL TO SAD PISES SVOJ TOK MISLI, BRADICE MOJA NEPOSTOJECA. SRCEEE KLAYEM JA SAD SI KO  MALA DALKILIDEAGKLINJA STA SE SDMIJES PERIO PEWRIO ]AJ CA AJ decorated_function

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    def count_time():
        start_time = time.time()
        function()
        end_time = time.time()
        final = end_time - start_time
        print(f"{function.__name__} run speed: {final}s") #! function.__name__ printa naziv funkcije
    return count_time

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()

 #! Da bi se sačuvao high_score moramo lokalno da ga usnimimo 
#! Snimamo ga kao .txt fajl

#! Fajl otvaramo ovako:
# file = open("Dan_24/my_file.txt")

#! Ako hocemo da manipulisemo fajlom onda mormao da ga .read()
# content = file.read()
# print(content)

#! Na kraju ako je otvoren moramo da ga zatvorimo sa .close() da smanjimo RAM memoriju koja se koristi
# file.close()

#* savet da otvaramo ovako sa with i sa as onda se ne otvara vec ako smo zavrsili onda se sam gasi
# with open("Dan_24/my_file.txt") as file:
#     content = file.read()
#     print(content)

#! ako hocemo da pisemo nesto u fajl moramo mode da postavimo da bude "w" (write), posto je po default read-only:
with open("Dan_24/my_file.txt", mode="a") as f:
    f.write("\nJA SAM HAKERMAN")

#! a ako hocemo da dodamo a ne da obrisemo onda umesto "w" onda dodajemo "a"
    
#! ako otvaramo fajl koji ne postoji, onda ce ga on sam napraviti i radi samo ako smo u "w" modu
with open("Dan_24/new_file.txt", mode="w") as f:
    f.write("\nJA SAM HAKERMAN")

#! Paths za fajlove
# fajlove
# folderi 
# root folder je sa jednom /, on je uglavnom C drive,

#! Absolute Path
#   primer putanje do foldera 
    #/Work/report/Project/talk.ppt
    
#! Working directory / Relative path
# ako radimo u Project folderu i hocemo da otvorimo talk onda otvaramo ovkao
    #.talk.ppt

#! .. znace da se otvara nesto za folder vise nego u kome smo mi
    
#! vezba otvaranje fajla sa desktopa / Apsolute path
with open("/Users/vlku_/OneDrive/Radna površina/anka.txt") as fajl:
    print(fajl.read())
#NASLA MENE ANKA A NE JA ANKU TJ KLIKNULI SMO ZAJEDNO ONAJ POTEZ RUKOM HAHA HEHE NOS RUKA

#! Vezba otvaranje fajla / Relative path
with open("../../Radna površina/anka.txt") as fajl:
    print(fajl.read())

#! Kviz
#1 - If you are writing code inside the main.py file to open the quiz.txt what would be the relative file path?
#   quiz.txt
    
#2 - What would be the absolute file path to the quiz.txt file?
#   /Users/my_project/quiz.txt
    
#3 - If you are writing code inside main.py, what is the relative file path to open quiz.txt?
#   ../my_files/quiz_files/quiz.txt
    
#! Mail Merge Challenge
# 1 - Version Control
#   1) Na primer sačuvao si neki fajl koji je radio kako treba
#   2) Sledeći put kada si radio sa njim dodao si neke stvari i sačuvao ih, ali sada nije radio kod kako treba
#   3) Version Control ti omogućava da se vratiš na BLIO KOJU prethodno sačuvanu verziju koda

# Navigacija do Radne površine
# cd /c/Users/vlku_/OneDrive/Radna\ površina

# Pravljenje foldera Story i navigacija u napravljen folder
# mkdir Story
# cd Story

# Pravljenje fajla u Story
# touch text1.txt

# Pravljenje fajla u Story i njegovo otvaranje u VS Codu
# code chapter1.txt

# Inicijalizacija GIT repository
# git init

# Da bi se pratile promene u Working Directory (Story), on mora da se nalazi u Staging Area
# Da bi proverili šta se nalazi u Staging Area koristimo:
# git status

# Sve stvari koje su crvene su stvari kod kojih se ne prate promene trenutno (untracked files )

# Da bi i njih dodali u praćenje koristimo:
# git add filename.extension

# Sada ako koristimo git status onda vidimo da je i taj fals sada zelen

# Ako hoćemo da commit odradimo, obavezno koristimo i -m (message koji i de uz git) uz samu poruku posle toga koja stoji u navodnicima "":
# git commit -m "Complete Chapter 1, initial commit"

# Da vidim sve promene (ko je napravi promenu, kada je napravio premnu, koja je message uz promenu i sam hash promene) koristim:
# git log

# Ako hoćemo da dodamo sve u Staging Area iz Workin Directory:
# git add .

# Da vidimi razlike koje su napravljene u fajlju
# git diff filename.extension

# Da se vratimo na prethodnu commit versiju
# git checkout chapter3.txt


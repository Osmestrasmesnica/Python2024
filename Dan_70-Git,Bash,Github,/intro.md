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

# 2 - GITHUB

# Povezivanje sa online repository odnosno pravljenje Remote Repository na GitHubu
# git remote add origin url_sa_githuba

# Slanje stvari iz Local Repository (sve sto smo do sada radili) u Remote Repository -u unite, origin na main branch
# git push -u origin main

## 3 - GITIGNORE

# Ako si pogresi nesto i stavio u staging a ne zelis tamo da bude onda koristis da sve sto je tamo izbacis iz staging
# git rm --cached -r . 

# Da se fajl ne pojavljuje na GitHub-u onda koristis .gitignore
# .gitignore i u njemu pises u svakom redu precizan naziv fajla koji ne zelis da se u GitHub repository nalazi (npr. .env,.DS_Store, secrets.txt...)
# Mozes da koristis komentare #
# Mozes da koristis *.txt i onda cese ignorisati svi fajlovi koji su text

# Link za gitignore githube, kopiras i ubacis ovo u svoj gitignore
# https://github.com/github/gitignore

## 4 - GIT CLONING

# Ako hoces da skines mozes da skines clon tvon repositorija ili da skines neciji vec napravljen repository
# git clone url_of_cloning_repository

# WORDLE
# git clone https://github.com/ritik48/Wordle-Game.git

## 5 - BRANCHING

# Da napravimo novi branch
# git branch new_branch_name

# da vdimo sve branches (* je kod ono u kom smo trenutno)
# git branch

# da promenimo u kom smo branch
# git checkout new_branch_name

# da spojimo brancheve moramo da budemo u main bracnh i onda koristimo merge, i otvorice se deo gde pisemo poruku a da izadjemo iz nje kucamo :q!
# git checkout main
# git merge new_branch_name
# :q!

# i da sve updatujemo na net koristimo 
# git push origin main -u 


# link za vezbanje GIT
# https://learngitbranching.js.org/

## Forking
# Kada se kopira i ostaje kod tebe nova kopija koju mozes da korigujes i nije vise vezana za stari originalni repository
# Kad se naprave neke promene na kopiji od originala i ukoliko neko hoce da nam posalje da nove, dodate stvari iz te kopije ubacimo u nas originalni repository (posto je ona forkovala a ne kopirala i ne moze sa radi "push").. to se onda zove "pull" request i onda ako mi se svidjaju onda cu da ih "merge".
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
  clear()
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
          print("\n\nRazdrala si se suviše glasno STRAŠNA ŽABA.")
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
          print("\n\nNailaziš na prijateljsko stvorenje zvano ORI i ono ti pomaže da se snađeš na ovoj tamnoj stazi.")
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
          print("Nakon nekog vremena, dolazite do LEKE i spašavate ga od dotadašnje dosade koju je ima bez VAS.∞∞∞ BRAVO ANČIKICEEEEEE !!∞∞∞ VOLI TE LEKA")
  
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
          print("\n\nOkrenula si se..... ZAŠTO?...očigledno nisi dovoljno horora gleda.... zna se ko sve prvi umire....STRAŠNOOOOO LJUBEEEE")
          print("Šuma je počela da menja oblik")
          print("Izgubila si se i nikada nisi pronašla Aleksu. Game over!")
  
  else:
      print("********************************************************************************************************************************")
      print("Nepravilan unos.. Da li znaš da pratiš uputstva? Da li si ikada sklapala policu od IKEA-e???. Game over.")
  
  # Dodajemo dodatnu funkcionalnost za kraj igre
  print("\n\nDa li želiš da probaš da nađeš Leku opet ili si odustala, msm za sada...mada, NIKAD NE ODUSTAJ OD LEKE")
  print("1. Da, želim ponovo da igram.")
  print("2. Ne, odustajem.")
  print("3. IZAĐI")
  
  choice_end = input("Izaberi (1, 2 ili 3): ")
  
  if choice_end == "1":
      print("\n\nNova avantura počinje! Srećno u potrazi za Aleksom!")
  elif choice_end == "2":
      clear()
      print("\n\nPfff...nećeš tako lako da odustaneš od LEKE...Daje ti LEKA ŠANSU DA SE ISKUPIŠ KAKO ZNAŠ I UMEŠ...smisli način a do tada probaj da ga nađeš!")
      time.sleep(8)  # Pauza od 5 sekundi
  elif choice_end == "3":
      print("\n\nGOTOVA IGRA. Hvala što si potražila Leku i što si prošla kroz Ankicinu avanturu!")
      break
  else:
      print("\n\nNepravilan unos. Igra će se završiti.")
      break
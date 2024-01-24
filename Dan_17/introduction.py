# #! PYTHON DAN 17
#! Creating Class

#! ATRIBUTI SU ONO STO OBJEKAT IMA
#! METODE SU ONO STO OBJEKAT RADI

# pises class pa nesto velikim slobom i :
# ovakvo nazivanje se naziva PascalCase
# a suprotno od toga je camelCase
# i postoji snake_case
class User:
    #pass # --> samo preskacemo ovo, da nema error-a
        
        #! Constructor
        # initialize of object - iniciranje objecta
        # specijalnom funkcijom __init__
        # sada kada god se koristi User() izacice ovo sto je u init
        # ovde dodajemo atribute
        def __init__(self, user_id, username):
            self.id = user_id
            self.username = username
            self.followers = 0 # --> mozemo i da odmah postavljamo default vrednost koja ne mora da se unosi prilikom inicijalizacije u zagrade
            self.following = 0 # --> mozemo i da odmah postavljamo default vrednost koja ne mora da se unosi prilikom inicijalizacije u zagrade
        
        #! Kreiranje metoda
            # uvek mora da ima self parametar u zagradi
        def follow(self, user):
              user.followers += 1
              self.following += 1

# #! pravljenje object koristeci class
# user_1 = User() # --> ako si definisao vec __init__ gore i imas u zagradama nesto, onda ti ovakvo pravljenje objecta izbacuje error

# #! dodajemo atribute
# user_1.id = "001"
# user_1.username = "aleksa"
              
user_1 = User("001", "aleksa")            

user_2 = User("002", "ankica")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)







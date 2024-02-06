# PYTHON DAN_30

############################### ERORS ###############################

# #! FileNotFound
# with open("a_file.txt") as f:
#     f.read()

# #! KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existing_key"]

# #! IndexError
# fruit_list = ["Jabuka", "Banana", "Kajsija"]
# fruit = fruit_list[3]

# #! TypeError
# text = "abc"
# print(text + 5)

#! Za handlovanje erorra bitno je:
# 1 - try: something that might cause an exception
# 2 - except: do this if there was an exception, ovde stavljamo alternativu ako se desi error
# 3 - else: do this if there were no exceptions
# 4 - finally: do this no matter what happens

try:
    file  = open("Dan_30_Errors_Exceptions_JSON/a_file.txt")
    a_dictionary = {"key":"value"}
    # print(a_dictionary["nepostojeci_kljuc"])
except FileNotFoundError:
    # print("There was an error")
    file = open("Dan_30_Errors_Exceptions_JSON/a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"Nema {error_message} key u ovom dictionary")
else: # --> ako je sve proslo gore u try kako treba i nije nista otislo u except onda se otvara ovaj ovde deo else
    content = file.read()
    print(content)
finally: # --> ovo se svkako izvrsava nebitno je da li je bilo exept ili else pre njega uvek ce se izvrsiti
    file.close()
    print("File was closed.")

#! Catching own Errors sa raise
    
#BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

#! ZADATAK 1 
#TODO Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something that is out of range just print a default output of "Fruit pie".
#TODO Example Input
#TODO ["Apple", "Pear", "Orange"]
#TODO Example Output
#TODO  Fruit pie
#TODO IMPORTANT: The exception handling should NOT allow each fruit to be printed when there is an exeption. e.g. it should not print out Apple pie, Pear pie and Orange pie, when there is an exerception it should only print "Fruit pie".
#TODO Hint:
#TODO You'll need to catch the IndexError exception.
#TODO You'll need the try, except and else keywords.

fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
  try:  
    fruit = fruits[index]
  except IndexError:
    print("Fruit pie")
  else:
    print(fruit + " pie")
make_pie(4)

#! ZADATAK 2

#TODO Use what you've learnt about exception handling to prevent the program from crashing.
#TODO Example Input
#TODO [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]
#TODO Using the eval() function we can create a list of dictionaries that looks like this:
#TODO facebook_posts = [
#TODO     {'Likes': 21, 'Comments': 2}, 
#TODO     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#TODO     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#TODO     {'Comments': 4, 'Shares': 2}, 
#TODO     {'Comments': 1, 'Shares': 1}, 
#TODO     {'Likes': 19, 'Comments': 3}
#TODO ]
#TODO Example Output: 86
#TODO Hint:
#TODO You'll need to catch the KeyError exception.
#TODO Posts without any likes can be counted as 0 likes.
#! Vodi racuna da mozes u okviru for petlje da stavljas try i except

# eval() function will create a list of dictionaries using the input
facebook_posts = eval([{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}])

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    post['Likes'] = 0
    total_likes = total_likes + post['Likes']
    # a moze samo i pass da se napise
    # pass
print(total_likes)


#! JSON library in python
# json.dump() wrtie
# json.load() read
# json.update() update

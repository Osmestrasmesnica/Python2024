import requests

parameters ={
    "amount" : 20, # --> number of questions to get from API request, max 50
    "category" : 17, # --> General Knowledge (9), Entertainment: Books (10), Entertainment: Film (11), Entertainment: Music (12), Entertainment: Musicals & Theatres (13), Entertainment: Television (14), Entertainment: Video Games (15), Entertainment: Board Games (16), Science & Nature (17), Science: Computers (18), Science: Mathematics (19), Mythology (20), Sports (21), Geography (22), History (23), Politics (24), Art (25), Celebrities (26), Animals (27), Vehicles (28), Entertainment: Comics (29), Science: Gadgets (30), Entertainment: Japanese Anime & Manga (31), Entertainment: Cartoon & Animations (32)
    "type" : "boolean" # --> type of question to get from API request, TRUE or FALSE
}


# response = requests.get(url="https://opentdb.com/api.php?amount=10&category=17&type=boolean")
response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
# print(data["results"])
     
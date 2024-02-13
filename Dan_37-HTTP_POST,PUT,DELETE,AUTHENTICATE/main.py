# PYTHON DAN-37
#! HTTP REQUESTS
# 1 - GET: requests.get() ask for data and we get that data in the response
# 2 - POST: requests.post() we give the data to external system and we are not interested in the response
# 3 - PUT: requests.put() update the data 
# 4 - DELETE: requests.delete() we delete the data

import requests
from datetime import datetime

PIXELA_TOKEN = "paokdfpoawkdopqwk"
PIXELA_USERNAME = "wlq"


PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"

PIXELA_GRPAH_ID = "graph1"
PIXELA_PIXEL_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{PIXELA_GRPAH_ID}"

# #! Napravili smo username
# user_paramethers = {
#     "token": PIXELA_TOKEN,
#     "username": PIXELA_USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=PIXELA_ENDPOINT, json=user_paramethers) #! ranije smo koristila params=user_paramethers
# print(response.text) # --> printamo response da vidimo da li je sve proslo

# graph_parameters = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ichou", # japanski zuta
#     "timezone": "Europe/Belgrade"
# }


headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# #! Mora i "headers" da se doda
# graph = requests.post(PIXELA_GRAPH_ENDPOINT, json=graph_parameters, headers=headers) 
# print(graph)
# # /v1/users/<username>/graphs/<graphID>
# #https://pixe.la/v1/users/wlq/graphs/graph1.html

#note Formatiranje vremena da ne moramo rucno da pisemo nego msamo autmatski da se unese
today = datetime.now()
# today = datetime(year=2024, month=2, day=12)

#note ovaj sada format moramo da napravimo da bude yyyyMMDD, koristiti link od ispod
#! https://www.w3schools.com/python/python_datetime.asp


#! Posting a pixel in graph
# /v1/users/<username>/graphs/<graphID>
pixel_paramthers = {
     "date": today.strftime("%Y%m%d"),
     "quantity": input("Unesi koliko si km danas prešao (peškice ili bicikla)..npr 13.53"),
}

pixel = requests.post(url=PIXELA_PIXEL_ENDPOINT, json = pixel_paramthers, headers=headers)
print(pixel.text)

#! Update and Delete a pixel
# UPDATE
# selected_date = datetime(year=2024, month=2, day=12).strftime("%Y%m%d")

# PIXELA_UPDATE_PIXEL_ENDPOINT = f"{PIXELA_PIXEL_ENDPOINT}/{selected_date}"

# update_pixel_parameters = {
#     "quantity": "5.01"
# }

# update = requests.put(url=PIXELA_UPDATE_PIXEL_ENDPOINT, json=update_pixel_parameters, headers=headers)
# print(update.text)

# DELETE
# delete = requests.delete(url=PIXELA_UPDATE_PIXEL_ENDPOINT, headers=headers)
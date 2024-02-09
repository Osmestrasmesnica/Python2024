#! PYTHON DAN 33

#! API - Application programming interface
#i set of commands, functions, protocols and objects that programmers can use to create software or interact with external systems

#TODO: Napraviti podatke za Nikolu Jokića da posle svake utakmice pošalje njegovu statistiku na broj telefona/email

import requests

# # Uzimanje podataka od API ENDPOINT
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response) # --> <Responese [200]>

# # Napise nam odmah koji je statuse i Error ne mormo rucno da pisemo (npr. error 404 = not found, eror 402 = not authorized...)
# response.raise_for_status()

# # ovako se vraca bilo koji text u svom trenutnom formatu .text
# # print(response.text)

# # ovako se vraca u json formatu text .json()
# data = response.json()
# # print(data)

# longitude = data["iss_position"]["latitude"]
# latitude = data["iss_position"]["longitude"]
# iss_position = (longitude,latitude)
# print(iss_position)

#! API with parameters
#info Mogu da budu Required i Optional

from datetime import datetime

# lat i lng su obavezni
LAT = 45.260658
LNG = 19.848549
position = (LAT, LNG) 
tzid = "Europe/Belgrade"

parameters = {
    "lat": LAT,
    "lng": LNG,
    "tzid": tzid,
    "formatted": 0
}

response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise, sunset)

time_now = datetime.now()
hour_now = time_now.hour
print(hour_now)

# ako nije formatirano, vreme (sunrise,sunset) i izgleda ovako 2024-02-09T16:59:48+01:00
# delimo prvo na 2 stvari u listi, separator je "T"
# uzimamo drugu stvar, odnosno [1] i delimo nju sa :
# uzimamo prvu stvar iz liste odnosno uzimamo vrednost za sate
# sunrise_time = sunrise.split("T")[1](":")[0]

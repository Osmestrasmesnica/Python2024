#! PYTHON DAN 35
#! API_KEY, TWILIO_API, PYTHON_ANYWHERE
#* procitati uvek dokmentaciju za API da bi znali sta tacno treba da trazimo

import requests
import os
from twilio.rest import Client

#! Twilio API
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#// account_sid = "AC08fbfe09551b415c715795d2e8ce05d2"
account_sid = os.environ.get("TWILIO_ACC_SID")
#// auth_token = "fe9fc4ee862314b18f0a1a38abef15b2"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

#//weather_api_python = "5383f987e34d22cfea68b5f8be44a4b7"
weather_api_python = os.environ.get("WEATHER_API_KEY")
print(weather_api_python)

LAT = 45.260658
LON = 19.848576

parameters = {
    "appid": weather_api_python,
    "lat": LAT,
    "lon": LON,
    "units": "metric",
    "cnt": 4, # number of timestamps that we need (da nam ne daje svih 40 za 5 dana unapred)
}

URL ="https://api.openweathermap.org/data/2.5/forecast?"

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
weather_data = response.json()

# id for weather for first 3 hours of forecast
print(weather_data["list"][0]["weather"][0]["id"])
print(weather_data["list"][1]["weather"][0]["id"])
print(weather_data["list"][2]["weather"][0]["id"])
print(weather_data["list"][3]["weather"][0]["id"])



#TASK print "Bring an Umbrella" if any of the weather condition codes is less than 700 in the next 12-hour window
will_rain = False
for hour_data in weather_data["list"]: # --> sada je hour_data = weather_data["list"][0, 1, 2 i 3]
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
# stavljamo da nam samo posalje jednom "Bring an Umbrella" ako bude kise a ne svaki put (4 puta za 6h) ako pada nonstop kisa 
if will_rain:
    print("Bring an Umbrella ☂️☂️☂️☂️")

#note ovo ispod je za slanje poruke ali se to placa i skida $$$
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#                 .create(
#                      body="Padaće kiša danas. Ne zaboravi da poneseš kišobran ☂️☂️☂️.",
#                      from_='+16592461250',
#                      to='+381643817840'
#                  )
# print(message.sid)
# print(message.status)

#! Environment variable
    
#note u terminal kucamo ovo ako je terminal powershell ili python
#info ls Env: sluzi da se izlistaju (ls = list) svi Environment varijable ili dir env:
# ls Env:
# dir env:
#info da vidimo doredjenu varijablu kucamo $env:NAZIVVARIJABLE (bez razmaka izmedju : i naziva varijable)
# $env:VARIABLE_NAME
#info setx da je postavimo da bude uvek vidljiva, tj postavljamo je kao system variable, mislim da ne moraju "" ali za svaki slucaj ih ostaviti ovde
# setx VARIABLE_NAME "value"

#note ako je terminal git bash
#info da vidimo sve varijable kucamo samo env
# env
#info da ubacimo novu varijablu kucamo samo export, VALUE nema "" oko sebe
# export NAME_OF_VARIABLE = VALUE 
import requests
from datetime import datetime
import smtplib
import random
import time

MY_LAT = 45.260658 # Your latitude
MY_LONG = 19.848549 # Your longitude
MY_EMAIL = "wlq.advisors@gmail.com"
PASSWORD = "xydzqpgueouacgkq"

def is_over_us():
    """Function to determine position within +5 or -5 degrees of the ISS position"""
    
    # get api position of iss
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"]) # --> mora float
    iss_longitude = float(data["iss_position"]["longitude"]) # --> mora float

    # check if the position is within +5 or -5 degrees of the ISS position
    if MY_LAT-5 < iss_latitude < MY_LAT+5 and MY_LONG-5 < iss_longitude < MY_LONG+5:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Europe/Belgrade"
}

def is_night():
    """Check if it is nighttime at our latitude and longitude"""

    # get api for our latitude and longitude
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) # --> mora int
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) # --> mora int

    # current hour
    time_now = datetime.now().hour

    # check if it is night time
    if sunrise < time_now < sunset:
        return True
    else:
        return False

while True:
    # run the code every 60 seconds.
    print("Running code")
    time.sleep(60)
    # if it is night and if it is above us within + - 5 degrees
    if is_over_us() and is_night():
        with open("Dan_33-API,ISS/International_Space_Station/motivation.txt", "r") as f:
            quotes = f.readlines()
            quote = random.choice(quotes).strip()
            motivational_text = "Look up! The International Space Station is passing over your location right now. Take a moment to appreciate the wonders of the universe and find inspiration in the boundless possibilities that lie ahead. Keep reaching for the stars!"
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs= MY_EMAIL,
                    msg=f"Subject: International Space Station is above you in Novi Sad at {MY_LAT}, {MY_LONG}/n\n{quote}\n\n{motivational_text}"
            )
            print("Poslata poruka")
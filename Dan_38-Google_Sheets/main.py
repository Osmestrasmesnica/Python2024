import requests
from datetime import datetime as dt
from dotenv import load_dotenv
import os

#Applay Secrets from .env file
load_dotenv()


NUTRITIONIX_USERNAME = os.getenv("NUTRITIONIX_USERNAME")
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")

SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_API_ENDPOINT = os.getenv("SHEETY_API_ENDPOINT")
SHEETY_AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")

# Neutral Language for Exercise
NLE_ENDPOINT = os.getenv("NLE_ENDPOINT")

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

params = {
    "query": input("Unesite koju ste aktivnost imali (ali na ENG):"),
    "weight_kg": 88,
    "height_cm": 185,
    "age": 28
}

response = requests.post(NLE_ENDPOINT, json=params, headers=headers)
response.raise_for_status()
result = response.json()
vezba = result["exercises"]

# new row of data in your Google Sheet for each of the exercises that you get back from the Nutritionix API
today = dt.now().strftime("%d/%m/%Y")
time = dt.now().strftime("%X")

# token za autentikaciju
bearer_headers ={
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
}

for exercise in vezba:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    add_row = requests.post(
        SHEETY_API_ENDPOINT, 
        json=sheet_inputs,
        headers=bearer_headers
        )
    print(add_row.text)
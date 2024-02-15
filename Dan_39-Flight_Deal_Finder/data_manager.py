import requests
import os
from dotenv import load_dotenv
from pprint import pprint 

#Applay Secrets from .env file
load_dotenv()

SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_API_ENDPOINT = os.getenv("SHEETY_API_ENDPOINT")
SHEETY_AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")
bearer_headers ={
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destionation_data(self):
        response = requests.get(SHEETY_API_ENDPOINT, headers=bearer_headers)
        response.raise_for_status()
        my_sheet = response.json()["prices"]
        pprint(my_sheet)
        self.destination_data = my_sheet
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_API_ENDPOINT}/{city["id"]}", json=new_data, headers=bearer_headers)
            print(response.text)
from pprint import pprint
import requests
from dotenv import load_dotenv
import os

load_dotenv()


SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")

SHEETY_AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")
bearer_headers ={
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=bearer_headers)
        data = response.json()
        pprint(data)  # Print the response JSON to inspect its structure
        # Assuming data structure is like {'destinations': [...]}, update the following line
        self.destination_data = data["prices"]  # Update key access based on the response structure
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=bearer_headers
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint, headers=bearer_headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_KIWI_API_KEY")

class FlightSearch:

    def get_destination_code(self, city_name):
        KIWI_URL = f"{TEQUILA_ENDPOINT}/locations/query"
        header = {"apikey": TEQUILA_API_KEY}
        parameters = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=KIWI_URL, headers=header, params=parameters)
        response.raise_for_status()
        result = response.json()["locations"]
        if result:
            code = result[0]["code"]
            return code
        else:
            print(f"No destination code found for {city_name}")
            return None
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 1,
            "curr": "EUR"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=parameters, headers=headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]  # Get the first flight data
            price = data.get("price")
            if price is not None:
                flight_data = FlightData(
                    price=price,
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0]
                )
                print(f"{flight_data.destination_city}: €{flight_data.price}")
                return flight_data
            else:
                print(f"No price information found for {origin_city_code} to {destination_city_code}")
                return None
        except (KeyError, IndexError) as e:
            print(f"Error processing flight data: {e}")
            return None

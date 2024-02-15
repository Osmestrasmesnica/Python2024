from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "BEG"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destionation_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(30*6))

for destination in sheet_data:
    try:
        flight = flight_search.check_flights(
            origin_city_code=ORIGIN_CITY_IATA,
            destination_city_code=destination["iataCode"],
            from_time=tomorrow,
            to_time=six_months_from_today
        )
    except Exception as e:
        print(f"Error processing flight data: {e}")
        continue
    
    if flight and flight.price < destination["lowestPrice"]:
        text = f"Low price alert! Only €{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        try:
            notification_manager.send_email(
                text=text,
                destination_email="wlq.advisors@gmail.com",
                price=flight.price,
                destination_city=flight.destination_city
            )
            print("Poslato")
        except Exception as e:
            print(f"Error occurred while sending email: {e}")

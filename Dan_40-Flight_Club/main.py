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

first_name = input(f"Welcome to WLQ Flight Club.\nWe find the best flight deals and email you.\nWhat is your first name?\n")
last_name = input(f"What is your last name?\n")
email = input(f"What is your email address\n")
email_verification = input(f"What is your email again\n")

if email == email_verification:
    print(f"Welcome to Flight Club WLQ {first_name} {last_name}.")

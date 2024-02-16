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


class UserManager():
    def __init__(self):
        self.first_name = input(f"Welcome to WLQ Flight Club.\nWe find the best flight deals and email you.\nWhat is your first name?\n").title()
        self.last_name = input(f"What is your last name?\n").title()
        self.email = input(f"What is your email address\n")
        self.email_verification = input(f"What is your email again\n")
        self.add_user()
        self.user_data = {}

    def get_users_data(self):
        response = requests.get(url=f"{SHEETY_API_ENDPOINT}/users", headers=bearer_headers)
        response.raise_for_status()
        users = response.json()["users"]
        pprint(users)
        self.user_data = users
        return self.user_data

    def add_user(self):
        while True:
            if self.email == self.email_verification:
                new_data = {
                    "user": {
                        "firstName": self.first_name,
                        "lastName": self.last_name,
                        "email": self.email,
                    }
                }                
                print(f"Welcome to Flight Club WLQ {self.first_name} {self.last_name}.") 
                response = requests.post(url=f"{SHEETY_API_ENDPOINT}/users", headers=bearer_headers, json=new_data)
                print(response.text)
                break  # Exit the loop if email verification is successful
            else:
                print("Email verification failed.")
                retry = input("Do you want to try again? (yes/no): ").lower()
                if retry != "yes":
                    print("User opted not to retry. Exiting user creation process.")
                    break  # Exit the loop if user opts not to retry
                else:
                    # Prompt the user to input email and verification email again
                    self.email = input("What is your email address?\n")
                    self.email_verification = input("What is your email again?\n")


user_manager = UserManager()
user_data = user_manager.get_users_data()
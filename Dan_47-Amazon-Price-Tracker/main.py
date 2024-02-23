import requests
from bs4 import BeautifulSoup
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

#Applay Secrets from .env file
load_dotenv()


headers = {
    "User-Agent": "Defined"
}

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")


############################################ FUNKCIJE ############################################ 

#info Umesto preko twilio sms-ove ja cu slati mailove preko smtp
def send_email(text, item_name):
    """Function for sending email with text parameter"""
    
    # Create a MIMEText object with formatted text
    email_content = MIMEText(text, "plain", "utf-8")

    # Create a MIMEMultipart object to attach the email content
    message = MIMEMultipart()
    message["Subject"] = f"Price drop ALERT by WLQ!!! Time to buy:{item_name}"
    message["From"] = MY_EMAIL
    message["To"] = MY_EMAIL
    message.attach(email_content)

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message.as_string())  


data = pd.read_csv("Dan_47-Amazon-Price-Tracker/amazon_to_buy.csv")
data_dict_list = data.to_dict(orient="records")

for url in data_dict_list:
    item_url = url["Url"]
    item_name = url["Naziv proizvoda"]
    item_lowest_price = url["Najmanja Cena"]
    print(f"Lowest price was:{item_lowest_price}€")
    time_to_buy = int(item_lowest_price)*1.05 # ako je 5% vise od najnize cene, onda hocu da kupim to
    response = requests.get(item_url, headers=headers).text
    soup = BeautifulSoup(response, "html.parser")
    try:
        price_of_item = soup.select_one("span.a-price-whole").getText().split(",")[0]
        price_int = int(price_of_item)
        if price_int*1.75 < item_lowest_price:
            print("There is no price for this item")
        elif time_to_buy < price_int:
            print(f"Current price:{price_of_item}€")
            print(f"Time to buy:{item_name} for {price_int} go to Amazon {item_url}")
            print("SENDING EMAIL")
            text = f"""Time to buy:{item_name} for {price_int} go to Amazon {item_url}"""
            try:
                send_email(text, item_name)
                print("Poslato")
            except Exception as e:
                print(f"Error occurred while sending email: {e}")
    except:
        print(f"No prices for {item_name}")



#! OVO RADI ALI SAM PREVISE PUTA TRAZIO REQUEST PA SAM MOZDA BANOVAN
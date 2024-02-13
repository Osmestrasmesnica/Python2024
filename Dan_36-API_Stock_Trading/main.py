import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

#Applay Secrets from .env file
load_dotenv()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_URL = "https://www.alphavantage.co/query?"
ALPHA_VANTAGE_STOCK_API = os.getenv("ALPHA_VANTAGE_STOCK_API") 

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

NEWS_API_URL = os.getenv("NEWS_API_URL")
NEWS_API = os.getenv("NEWS_API")

############################################ FUNKCIJE ############################################ 

#info Umesto preko twilio sms-ove ja cu slati mailove preko smtp
def send_email(text):
    """Function for sending email with text parameter"""
    
    # Create a MIMEText object with formatted text
    email_content = MIMEText(text, "plain", "utf-8")

    # Create a MIMEMultipart object to attach the email content
    message = MIMEMultipart()
    message["Subject"] = f"{STOCK}:{up_down}{diff_percent}"
    message["From"] = MY_EMAIL
    message["To"] = MY_EMAIL
    message.attach(email_content)

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message.as_string())  
    

############################################ API REQUESTS ############################################
        
#! API FOR SELECTED STOCK
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_STOCK_API
}

response = requests.get(url=STOCK_URL, params=parameters)
response.raise_for_status()
stock_data = response.json()

daily_stock_data = stock_data["Time Series (Daily)"]
#note list_of_stock_data = [data["4. close"] for data in daily_stock_data.values()] # --> moze i ovako
list_of_stock_data = [value for (key, value) in daily_stock_data.items()] 

# Podaci za juce i za prekuce
yesterday_data = list_of_stock_data[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = list_of_stock_data[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percent)

#! IF DIFFERENCE PERCENTAGE IS GREATER THEN 5 GET NEWS FOR STOCK
if abs(diff_percent) > 1:

    #!API FOR NEWS FOR SELECTED STOCK
    news_params = {
        "qInTitle": COMPANY_NAME,  # Keywords or phrases to search for in the article title and body.
        "apiKey": NEWS_API,
    }

    news = requests.get(NEWS_API_URL, params=news_params)
    news.raise_for_status()
    articles = news.json()["articles"]
    three_articles = articles[:3] # --> get last 3 articles
    # print(three_articles)

    for article in three_articles:
        title = article["title"]
        description = article["description"]
        url = article["url"]
        text = f"""Title: {title}\nBrief: {description}\nLink: {url}\n"""
        try:
            send_email(text)
            print("Poslato")
        except Exception as e:
            print(f"Error occurred while sending email: {e}")
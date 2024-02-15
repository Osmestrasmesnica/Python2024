from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

class NotificationManager:
    def send_email(self, text, destination_email, price, destination_city):
        """Function for sending email with text parameter"""
        
        # Create a MIMEText object with formatted text
        email_content = MIMEText(text.format(price=price, destination_city=destination_city), "plain", "utf-8")

        # Create a MIMEMultipart object to attach the email content
        message = MIMEMultipart()
        message["Subject"] = f"Jeftini let za €{price} do {destination_city}"
        message["From"] = MY_EMAIL
        message["To"] = destination_email
        message.attach(email_content)

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=destination_email, msg=message.as_string())


# Example usage:
# notification_manager = NotificationManager()
# notification_manager.send_email("Example text for the email.", "recipient@example.com")

from flask import Flask, render_template,request
import requests
import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Applay Secrets from .env file
load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', "GET"])
def contact():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name, email, phone, message)
        send_email(name, email, phone, message)
        poruka = "Uspesno poslate stvari"
        return render_template("contact.html", poruka = poruka)
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

def send_email(name, email, phone, message):
    # Create a MIMEText object with UTF-8 encoding
    email_message = MIMEText(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}", _charset="utf-8")
    email_message["Subject"] = "Poruka sa bloga - WLQ Innovations BLOG"
    email_message["From"] = MY_EMAIL
    email_message["To"] = MY_EMAIL
    
    # Establish connection and send the email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.send_message(email_message)

if __name__ == "__main__":
    app.run(debug=True, port=5001)

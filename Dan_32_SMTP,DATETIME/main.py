# PYTHON DAN 31

import smtplib
from email.message import EmailMessage
import ssl
import datetime as dt
import random


my_email = "wlq.advisors@gmail.com"
email_receiver = "wlq.advisors@hotmail.com"
PASSWORD = "xydzqpgueouacgkq"

# subject = "Proba slanja maila preko Phytona"
# body = """
# What is Lorem Ipsum?
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

# Why do we use it?
# It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


# Where does it come from?
# Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

# The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
# """

# em = EmailMessage()
# em["From"] = my_email
# em["To"] = email_receiver
# em["Subject"] = subject
# em.set_content(body)

# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
#     smtp.login(my_email, PASSWORD)
#     smtp.sendmail(my_email, email_receiver, em.as_string())


# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=PASSWORD)
# connection.sendmail(my_email, "wlq.advisors@hotmail.com", msg=" Subject: Hello \n\n Body of email..")
# connection.close()
    
# Verzija sa kursa

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=PASSWORD)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="wlq.advisors@hotmail.com", 
#         msg=" Subject: Hello \n\n Body of email.."
#     )

# vreme = dt.datetime.now()
# dan_u_nedelji = vreme.weekday()
# print(dan_u_nedelji)
# date_of_birth = dt.datetime( day=15, month=12, year=1995, hour=4)
# print(date_of_birth)


#! Zadatak 1
# Poslati motivacionu poruku svakog petka na nekoliko mailova
# Koristiti: datetime module, quotes.txt za citate, random module za biranje random quote, smtplib za slanje mailova

dan_u_nedelji = dt.datetime.now().weekday()
print(dan_u_nedelji)

if dan_u_nedelji == 4:
    with open("Dan_32_SMTP,DATETIME/quotes.txt", "r") as f:
        quotes = f.readlines()
        quote = random.choice(quotes)
        print(quote)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=PASSWORD)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="ankicamilovanovic2@gmail.com", 
                msg=f" Subject: Motivacioni govori - WLQ \n\n{quote}\n Voli te Leka"
            )
        print("Poslata poruka")

#! Zadatak 2 - Automated Birthday wisher


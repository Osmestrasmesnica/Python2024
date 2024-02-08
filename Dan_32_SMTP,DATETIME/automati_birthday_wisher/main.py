##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

#! Napraviti ovo da bude kao environment variable
MY_EMAIL = "wlq.advisors@gmail.com"
PASSWORD = "xydzqpgueouacgkq"

# Compute current month and day
current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day

# citanje csv pomocu pandas
data = pd.read_csv("Dan_32_SMTP,DATETIME/automati_birthday_wisher/birthdays.csv")

# Iskljucivo za testiranje
test_month = dt.datetime(2024,11,19)

# Random letter number for template selection
random_letter_number = random.randint(1,3)

#! Looping through DataFrames - rows of a data frame
for index, row in data.iterrows():
    if int(row.month) == current_month and int(row.day) == current_day:
        # Pravljenje poruke i snimanje kopije
        with open(f"Dan_32_SMTP,DATETIME/automati_birthday_wisher/letter_templates/letter_{random_letter_number}.txt", "r") as f:
            letter_template = f.read()
            new_letter = letter_template.replace("[NAME]", row["name"])

        # Ovo je visak ali ja hocu da imam kopiju koja se salje
        with open(f"Dan_32_SMTP,DATETIME/automati_birthday_wisher/letter_templates/letter_{random_letter_number}_to_{row["name"]}_sent.txt", "w") as f:
            f.write(new_letter)
        
        # Slanje emaila
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr= MY_EMAIL, 
                to_addrs= row.email,
                msg=f"Subject: SREĆAN ROĐENDAN \n\n{new_letter}".encode("utf-8")
            )
        print("Poslata poruka")


#! NA KRAJU SVEGA MOZES DA AUTMATIZUJES DA RADI KOD ZAUVEK U POZADINI NA SAJTU
#https://www.pythonanywhere.com/user/Zitkapnazaburgavinu/tasks_tab/
import smtplib
from datetime import datetime
import random

sender_email="amadeus40585@gmail.com"
app_password="tuxjnmozogyebrun"
receiver_email="avaneesh40585@gmail.com"

with open(file="quotes.txt") as quotes_file:
    quotes_list=quotes_file.readlines()
random_quote=random.choice(quotes_list)

now=datetime.now()
if(now.weekday()==0):
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email,password=app_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=f"Subject:Monday Motivational Quote\n\n{random_quote}"
            )
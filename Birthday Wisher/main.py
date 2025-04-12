import pandas as pd
import datetime as dt
import random
import smtplib
# *-------------------------- DATA MANAGEMENT -------------------------------* #
now=dt.datetime.now()

sender_email="amadeus40585@gmail.com"
app_password="tuxjnmozogyebrun"

birthdays_df=pd.read_csv("birthdays.csv")
birthdays_dict=birthdays_df.to_dict(orient="records")

letter_list=["./letter_templates/letter_1.txt","./letter_templates/letter_2.txt","./letter_templates/letter_3.txt"]
random_letter=random.choice(letter_list)
# *------------------------ CHECK & SEND EMAIL -------------------------------* #
for birthday in birthdays_dict:
    if(birthday["month"]==now.month and birthday["day"]==now.day):
        with open(file=random_letter) as initial_letter:
            intial_content=initial_letter.read()
            final_content=intial_content.replace("[NAME]",birthday["name"])
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=sender_email,password=app_password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy Birthday\n\n{final_content}"
                )





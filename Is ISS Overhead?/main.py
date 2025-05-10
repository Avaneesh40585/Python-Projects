import requests
from datetime  import datetime
import smtplib
import time
# *------------------------------ POSITION SETUP -------------------------------* #
MY_LAT=22.531255 # Enter your latitude here
MY_LONG=75.923722 # Enter your longtitude here
sun_parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}
def is_iss_overhead():
    if(abs(iss_latitude-MY_LAT)==5 and abs(iss_longitude-MY_LONG)==5 and (hour_now>=sunset_hour and hour_now<=sunrise_hour)):
        return True
        
# *------------------------------ RESPONSE SETUP --------------------------------* #
iss_response=requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data=iss_response.json()
iss_latitude=iss_data["iss_position"]["latitude"]
iss_longitude=iss_data["iss_position"]["longitude"]

sun_response=requests.get(url="https://api.sunrise-sunset.org/json?lat=%2722.531255%27&lng=%2775.923722%27&formatted=0")
sun_response.raise_for_status()
sun_data=sun_response.json()
sunrise_hour=(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour=(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
hour_now=datetime.now().hour

# *------------------------------- SEND EMAIL-----------------------------------* #
sender_email="sender email here"
app_password="your password here"
receiver_email="reciever email here"

def send_mail():
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=sender_email,password=app_password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=receiver_email,
                msg="Subject:ISS Overhead\n\nThe ISS is currently flying over you, look up in the sky to get a glance of it"
                )
while True:
    time.sleep(60)
    if(is_iss_overhead()):
        send_mail()

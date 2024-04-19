import smtplib
import requests
from datetime import datetime
import time

MY_LAT =   # Your latitude
MY_LONG =   # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
flag = False


if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
    flag = True
else:
    flag = False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "America/New_York",
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour

while True:
    time.sleep(60)
    if flag == True and sunrise >= hour_now or hour_now >= sunset:
        my_email = "INSERT YOUR EMAIL"
        my_password = "EMAIL APP PASSWORD"
        connection = smtplib.SMTP("smtp.gmail.com")#find your smtp provider extension
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="INSERT RECEIVERS ADDRESS",
                            msg="Subject:The ISS is over you\n\nLook up at the sky!")


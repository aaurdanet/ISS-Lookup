# ISS-Lookup

This Python script allows you to track the International Space Station (ISS) in real-time and receive email notifications when it's passing over your location during the night.
Requirements

Python 3.x
smtplib library (for sending emails)
requests library (for making HTTP requests)
datetime module (for handling date and time)
time module (for introducing delays)

Installation

Clone or download this repository to your local machine.
Ensure you have Python installed.
Install required dependencies by running: pip install requests

Usage

Set your latitude (MY_LAT) and longitude (MY_LONG) in the script to match your location.
Replace "INSERT YOUR EMAIL" and "EMAIL APP PASSWORD" with your email credentials.
Specify the receiver's email address in "INSERT RECEIVERS ADDRESS".
Run the script using Python: python iss_tracker.py.
The script will continuously check if the ISS is passing over your location during the night. If conditions are met, it will send you an email notification.

Notes

Ensure your email provider allows SMTP connections. If you're using Gmail, you might need to generate an app password since Gmail doesn't allow less secure apps by default.
The script uses the Open Notify API to get the ISS's current location and the Sunrise-Sunset API to get sunrise and sunset times for your location.
It checks if the ISS is within 5 degrees of your position and if it's during the night to send notifications.
The script will keep running indefinitely. You can stop it manually by pressing Ctrl + C.

import requests
import os

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # <-- this reads the .env file

OWM_endpoint="https://api.openweathermap.org/data/2.5/forecast"

# Download the helper library from https://www.twilio.com/docs/python/install



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
my_key=os.environ["api_key"]




weather_paras={
    "lat":10.800371,
    "lon":79.190313,
    "appid":my_key,
    "cnt":4,
}
response=requests.get(OWM_endpoint,params=weather_paras)
response.raise_for_status()
jsonform=response.json()

will_rain=False
for i in range(0,4):
    firstake=jsonform["list"][i]["weather"][0]["id"]
    if firstake<700:
        will_rain=True
    else:
        pass

if(will_rain):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It is going to rain today bring an ☂️",
        from_=yourtwilionumber,
        to=yourpersonalnumber,

    )

    print(message.status)

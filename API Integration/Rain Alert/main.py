import os
import requests
from twilio.rest import Client

OWP_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
IST_LAT = 40.9912955  # Istanbul's latitude
IST_LNG = 29.0245631  # Istanbul's longitude

account_sid = os.environ.get("OWM_ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": IST_LAT,
    "lon": IST_LNG,
    "appid": API_KEY,
    "cnt": 4  # The  number of timestamps to fetch weather data for the next 12 hours.
}

response = requests.get(url=OWP_URL, params=parameters)
response.raise_for_status()
data = response.json()
print(data)

will_rain = False
for rec in data["list"]:
    if int(rec["weather"][0]["id"]) < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂︎⛆",
        from_="whatsapp:+14155238886",
        # from_="+12186667623",
        to="whatsapp:+905355599567"
        # to="+905355599567",
    )

    print(message.body)

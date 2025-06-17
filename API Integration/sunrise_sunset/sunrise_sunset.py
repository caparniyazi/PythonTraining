import requests
import datetime as dt
import smtplib
import time

IST_LAT = 40.9912955  # Istanbul's latitude
IST_LNG = 29.0245631  # Istanbul's longitude

PLACEHOLDER = "[NAME]"
EMAIL = "capar.niyazi.tr@gmail.com"
PWD = "xxxx xxxx xxxx xxxx"
SMTP_PROVIDER = "smtp.gmail.com"


def send_email():
    with smtplib.SMTP(SMTP_PROVIDER) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=EMAIL, password=PWD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:Look Up👆.\n\nThe ISS is above you in the sky."
                            )


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    # If the ISS is close to my current position
    if (IST_LAT - 5 <= iss_lat <= IST_LAT + 5) and (IST_LNG - 5 <= iss_lng <= IST_LNG + 5):
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": IST_LAT,
        "lng": IST_LNG,
        "formatted": 0,
        "tzid": "Europe/Istanbul"
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()
    response.raise_for_status()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:  # It's currently dark.
        return True
    else:
        return False


while True:
    time.sleep(60)  # Sleep for 60 secs.
    if is_iss_overhead() and is_night():
        print("Look up")
        send_email()
    else:
        print("Not yet")

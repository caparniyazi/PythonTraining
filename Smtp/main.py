import random
import datetime as dt
import smtplib


def send_email(content):
    my_email = "capar.niyazi.tr@gmail.com"
    my_password = "xxxx xxxx xxxx xxxx"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="niyazi.capar@xyz.com",
                            msg=f"Subject:Quote of the day.\n\n{content}."
                            )


# Sending a random quote of the day.
today = dt.datetime.now()
the_weekday = today.weekday()

if the_weekday == 5:
    with open("quotes.txt") as in_file:
        quotes = in_file.readlines()
        quote = random.choice(quotes)
        send_email(quote)

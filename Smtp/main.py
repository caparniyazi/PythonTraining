import datetime as dt
import smtplib
import random
import pandas

PLACEHOLDER = "[NAME]"
EMAIL = "capar.niyazi.tr@gmail.com"
PWD = "xxxx xxxx xxxx xxxx"
SMTP_PROVIDER = "smtp.gmail.com"


def send_email(contents, recipient_address):
    with smtplib.SMTP(SMTP_PROVIDER) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=EMAIL, password=PWD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=recipient_address,
                            msg=f"Subject:Quote of the day.\n\n{contents}."
                            )


def check_birthdays():
    data_frame = pandas.read_csv("birthdays.csv")
    # print(data_frame)

    now = dt.datetime.now()
    today_tuple = (now.month, now.day)
    birthdays_dic = {(data_row.month, data_row.day): data_row for (index, data_row) in data_frame.iterrows()}

    if today_tuple in birthdays_dic:
        birthday_person = birthdays_dic[today_tuple]
        file_path = f"letters/letter_{random.randint(1, 3)}.txt"

        with open(file_path) as letter_file:
            letter_contents = letter_file.read()
            contents = letter_contents.replace(PLACEHOLDER, birthday_person["name"])
            send_email(contents, birthday_person["email"])


check_birthdays()
# my_dict = data_frame.to_dict(orient="records")
# for item in my_dict:
#     if item["month"] == now.month and item["day"] == now.day:
#         name = item["name"]
#         with open("letters/letter_1.txt") as letter_file:
#             letter_contents = letter_file.read()
#             new_letter = letter_contents.replace(PLACEHOLDER, name)
#             send_email(new_letter)

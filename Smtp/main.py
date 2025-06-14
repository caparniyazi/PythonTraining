import smtplib

my_email = "capar.niyazi.tr@gmail.com"
my_password = "xxxx xxxx xxxx xxxx"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # Secure the connection
    connection.login(my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="niyazi.capar@xyz.com",
                        msg="Subject:Hello world.\n\nHello everyone."
                        )

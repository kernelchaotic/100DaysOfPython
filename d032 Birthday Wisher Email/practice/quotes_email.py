import smtplib
import datetime as dt
import random

my_email = 'emailofchoice@gmail.com'
password = 'password'

now = dt.datetime.now()
current_day = now.weekday()

if current_day == 2:
    with open('quotes.txt') as quotes:
        lines = quotes.read().splitlines()
        selected_quote = random.choice(lines)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='recipientemail@yahoo.com',
                            msg=f"Subject: Hello, Name!\n\n {selected_quote}")

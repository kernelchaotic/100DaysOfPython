import smtplib
import datetime as dt
import pandas as pd

# Constants
MY_EMAIL = 'emailofchoice@gmail.com'
PASSWORD = 'password'

# Check to see what the month and day are
date = dt.datetime.now()
today = (date.month, date.day)

# use pandas to read birthdaybank.csv and create a dictionary of birthdays
birthday_bank = pd.read_csv('birthdaybank.csv')
birthdays = {(data_row['month'],data_row['day']): data_row for (index, data_row) in birthday_bank.iterrows()}

# check if date is a birthday then send email
if today in birthdays:
    email_recipient = birthdays[today]
    with open('birthday_letter.txt', 'r') as letter:
        text = letter.read()
        body = text.replace('[NAME]', email_recipient['name'])

# Send birthday email on the correct day to recipients
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs='recipientemail@yahoo.com', msg=body)

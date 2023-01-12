import smtplib
import datetime as dt

my_email = 'chosenemail@gmail.com'
password = 'apppassword'

# establish connection to email service
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

    # encrypts email contents and makes connection secure
    connection.starttls()

    # login to email
    connection.login(user=my_email, password=password)

    # send email to recipient
    connection.sendmail(from_addr=my_email, to_addrs='testingkit007@yahoo.com',
                        msg="Subject: Hello, D!\n\n This one shouldn't get spam-filtered :D")

# if not using with, close connection with
# connection.close()



now = dt.datetime.now()

date_of_birth = dt.datetime(year=2002, month=5, day=25, hour=19, minute=7)

print(date_of_birth)
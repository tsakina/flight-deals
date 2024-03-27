from twilio.rest import Client
import smtplib

ACCOUNT_SID = "****************"
TWILIO_AUTH_TOKEN = "***************"
TWILIO_VIRTUAL_NUMBER = "**********"
TWILIO_VERIFIED_NUMBER = "**********"

MY_EMAIL = "******@gmail.com"
MY_PASSWORD = "*********"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, message, emails):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8'))


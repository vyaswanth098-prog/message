from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_number = os.getenv('TWILIO_NUMBER')
to_number = os.getenv('MY_NUMBER')

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello, Yaswanth",
    from_=from_number,
    to=to_number
)

print(f"Message SID: {message.sid}")


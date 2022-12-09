# Import the necessary libraries
from twilio.rest import Client

# Set up your Twilio account and get a WhatsApp-enabled phone number
account_sid = "YOUR ACCOUNT SID"
auth_token = "YOUR AUTH TOKEN"
client = Client(account_sid, auth_token)
from_whatsapp_number = "+1 YOUR WHATSAPP NUMBER"

# Define the logic and functionality of your bot
def handle_message(message):
  # If the message contains the word "hello"
  if "hello" in message.lower():
    # Respond with "Hello there!"
    response = "Hello there!"
    client.messages.create(
      from_=from_whatsapp_number,
      body=response,
      to=message.from_
    )

# Listen for incoming messages and handle them using the defined logic
@client.on_message()
def message_received(message):
  handle_message(message)

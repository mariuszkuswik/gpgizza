# Import the required libraries
from fbchat import Client
from fbchat.models import *

# Create a custom client class
class Messenger(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        # Method to handle incoming messages
        print(f"Message from {author_id}: {message_object.text}")

# Define your Facebook access token
access_token = "YOUR_ACCESS_TOKEN"

# Create a Messenger client
client = Messenger("YourUsername", "YourPassword", session_cookies=None, user_agent=None)

# Login to Facebook
client.login()

# Send a text message
recipient_id = "USER_ID_OR_GROUP_ID"
message = "Hello, this is a test message from my Python Messenger app!"
client.send(Message(text=message), thread_id=recipient_id, thread_type=ThreadType.USER)

# Logout from Facebook
client.logout()

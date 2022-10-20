from twilio.rest import Client
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

urls = os.environ.get("URL")


def checkingName(name):

    try:
        comic_name = name
        with open("names.txt", "r") as f:
            if comic_name in f.read():
                return True
    except Exception as e:
      return e
    


def sendMessage(name):

    try:
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        to_number = os.environ.get('TO')
        from_number = os.environ.get('FROM')

        # Your Account SID from twilio.com/console
        account_sid = account_sid
        # Your Auth Token from twilio.com/console
        auth_token  = auth_token

        client = Client(account_sid, auth_token)
    
        message = client.messages.create(to=to_number,from_=from_number, body=f"{name} comics Out Today Check out now")
        
    except Exception as e:
      return e
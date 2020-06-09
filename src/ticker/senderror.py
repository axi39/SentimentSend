### Sentiment Send ###
### GitHub axi39   ###
### See LICENSE.md in /docs/LICENSE ###

#FILE TEST SUCCESSFUL, 04.06.2020

from twilio.rest import Client
import os


def send_ticker_error():
    #Message composition.
    message_body = "Invalid ticker or too many API calls in a short period.  Please try again."
    
    #Twilio SMS message.  REQUIRES TWILIO ACCOUNT CREDENTIALS.
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=message_body,
                        from_='SOURCE NUMBER',
                        to='TARGET NUMBER'
                    )

if __name__ == "__main__":
    send_ticker_error()


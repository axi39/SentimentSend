### Sentiment Send ###
### GitHub axi39   ###
### See LICENSE.md in /docs/LICENSE ###


import ingest
import sentiment
from twilio.rest import Client
import os



if __name__ == "__main__":

    #Scrape and ingest data into DB from news sources.  See /src/ingest.py
    ingest.ingest_news("nyt", "https://www.nytimes.com/", "h2")
    ingest.ingest_news("bbc", "https://www.bbc.co.uk/news", "h3")

    #Prepare for SMS by aggregating sentiment.  See /src/sentiment.py
    to_send = sentiment.clean()
    
    #Categorize/map most recent sentiment aggregate score.
    if float(to_send.tail(1)['sentiment']) > 0:
        x = "positive"
    elif float(to_send.tail(1)['sentiment']) == 0:
        x = "neutral"
    else:
        x ="negative"
    
    #Message composition.
    message_body = "The mean sentiment of both BBC News & NYTimes is as follows: \n" + to_send.to_string(header=False) + "\n which is considered: " + x + "."
    
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

    #Validate message sent by identifier.
    print(message.sid)
    

    
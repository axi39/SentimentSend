### Sentiment Send ###
### GitHub axi39   ###
### See LICENSE.md in /docs/LICENSE ###

#IN PROGRESS, 04.06.2020


from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import time

#Global time variable, executes regardless of __name__ == "__main__"
timestamp = datetime.today().strftime('%Y-%m-%d-%H:%M')


#Instantinate Flask app with __name__ current module.
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    '''
    Flask backend to reply to SMS

    parameter(s): news article source name (str), news site URL (str), HTML header type for article titles (str)

    returns: void.

    '''
    #Instantinate response object from Twilio.
    resp = MessagingResponse()
    
    #insms = request.form.get("Body")

    #Reply
    resp.message("Test Successful")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
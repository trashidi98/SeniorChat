import os
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_api_key_sid = os.environ.get('TWILIO_API_KEY_SID')
twilio_api_key_secret = os.environ.get('TWILIO_API_KEY_SECRET')
twilio_phone_number = os.environ.get('TWILIO_PHONE_NUMBER')
twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

def video_access_token(roomId: str, username:str) -> str:
    token = AccessToken(twilio_account_sid, twilio_api_key_sid,
                        twilio_api_key_secret, identity=username,
                        ttl=3600)
    token.add_grant(VideoGrant(room=roomId))
    return token.to_jwt() # This str() is done to work with (slightly) older flask/python version.

def send_sms(numberToSendTo: str, body: str):
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body=body,
        from_=twilio_phone_number,
        to=numberToSendTo,
    )
    print(message.sid)

if __name__ == "__main__":
    send_sms("+17814924791", 'hi')
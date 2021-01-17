# Setting up Environment Variables

```bash
cd api/
touch .env
```

- Add the following to .env

```
TWILIO_ACCOUNT_SID=<XXX>
TWILIO_API_KEY_SID=<XXX>
TWILIO_API_KEY_SECRET=<XXX>
TWILIO_AUTH_TOKEN=<XXX>
TWILIO_PHONE_NUMBER=<XXX>
```

# Sample API requests with curl

```bash
curl -i -H "Content-Type: application/json" http://localhost:5000/api/v1/contacts -H "user_id: 0" # Get Contacts

curl -i -H "Content-Type: application/json" http://localhost:5000/api/v1/contact -H "user_id: 0" -X POST -d '{"friend_user_name": "saif1"}' # POST Contact (add contact)

curl -i -H "Content-Type: application/json" http://localhost:5000/api/v1/contact -H "user_id: 0" -X DELETE -d '{"friend_user_name": "saif1"}' # DELETE Contact
```

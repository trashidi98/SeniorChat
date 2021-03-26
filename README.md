# SeniorChat 

SeniorChat is a video chat application based on **Twilio** Video API as the main engine. The backend was built with **Django**, frontend in **React**, and uses a **SQLLite** backend. The app also leveraged the use of **Google's FireBase Authentication** service so users could use their Gmail to sign up. 

The purpose of the application was to simplify the video chat experience for senior citizens. Features like a **simple UI**, **easy sign-up** (using FireBase Authentication) and **video rooms** where family and friends could drop in and say hi! 

This application was built for a hackathon during hackUCDavis, at the height of COVID-19. This was particularly challenging because there was no in-person communication and thus no guaruntee that your partners would stick around. I am *very* proud of our team who worked on this project throughout the weekend and never bailed. We were even in different time zones! 

You can find our demo and submission here: https://devpost.com/software/seniorchat 

## Setting up Environment Variables

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

## Sample API requests with curl

```bash
curl -i -H "Content-Type: application/json" http://localhost:5000/api/v1/contacts -H "user_id: 0" # Get Contacts

curl -i -H "Content-Type: application/json" http://localhost:5000/api/v1/contact -H "user_id: 0" -X POST -d '{"friend_user_name": "saif1"}' # POST Contact (add contact)

curl -i -H "Content-Type: application/json" http://localhost:5000/api/v1/contact -H "user_id: 0" -X DELETE -d '{"friend_user_name": "saif1"}' # DELETE Contact
```

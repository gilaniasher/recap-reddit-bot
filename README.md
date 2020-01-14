# Recap Reddit Bot
A Reddit bot that uses the SMMRY API to summarize any article (inspired by TL;DR bot)

# To run your own instance of this bot

## Create a Reddit account (or use an existing)
Follow instructions to create your own Reddit bot to get your client ID and client Secret.

## Add a praw.ini file
Create a file called praw.ini in the same directory recap_bot.py is located.
You will need your client ID, client Secret, and the username/password for your Reddit account.
Write anything for the user_agent.
Then fill in the file using the following template:
```
[recap-bot]
client_id=
client_secret=
password=
username=
user_agent=
```

## Add a smmry_credentials.py file
You will need to go to [SMMRY](www.smmry.com) and create a free account to get your own api key.
Then create the file smmry_credentials.py in the same directory recap_bot.py is located.
Then fill in the file using the following template:
```
api_key = '{YOUR_API_KEY}'
```

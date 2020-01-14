# Recap Reddit Bot
A Reddit bot that uses the SMMRY API to summarize any linked article.

# Example Usage
When the script is running, go into the specified Subreddit (testingground4bots by default), and comment something in the form:

```
!recapbot www.{any-article}.com
```

Recap Bot will query the SMMRY API and reply to this comment with the summarized version of the article.

# Running this Bot

* Create a Reddit account (or use an existing)
* Go to [Reddit Apps](https://www.reddit.com/prefs/apps/)
* Create a Reddit App, select script, and put anything for the About URL and Redirect URI
* Register an account with [SMMRY](https://smmry.com/partner)
* Note down the API Key


## Add a praw.ini File
Add a praw.ini file in the same directory as recap_bot.py. The below username/password are for the Reddit account with the Reddit Bot App.
Then fill in the file using the following template:

```
[recap-bot]
client_id=
client_secret=
password=
username=
user_agent=
```

## Add a smmry_credentials.py File
Add a smmry_credentials.py in the same directory as recap_bot.py.
Then fill in the file using the following template:

```
api_key = '{YOUR_API_KEY}'
```

## Run the Bot
Run ```python3 recap_bot.py``` and you're finished! Recap Bot will continue to look for comments that start with !recapbot to respond to them.

You can change this keyword trigger by changing the variable ```keyphrase``` in ```recap_bot.py```. You can change the Subreddit by changing the parameter in the ```subreddit``` variable in the same script.

You can run this script on an AWS EC2 instance to have the script run indefinitely.

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
* Note down the Client ID and the Client Secret
* Register an account with [SMMRY](https://smmry.com/partner)
* Note down the API Key


## praw.ini File
Fill in the ```praw.ini``` file. Use the username and password for the Reddit account associated with your Bot. 


```
[recap-bot]
client_id=
client_secret=
password=
username=
user_agent=
```

## smmry_credentials.py File
Fill in the ```smmry_credentials.py``` file using your SMMRY API Key.

```
api_key = '{YOUR_API_KEY}'
```

## Run the Bot
Run ```python3 recap_bot.py``` and you're finished! Recap Bot will continue to look for comments that start with !recapbot to respond to them.

You can change this keyword trigger by changing the variable ```keyphrase``` in ```recap_bot.py```. You can change the Subreddit by changing the parameter in the ```subreddit``` variable in the same script.

You can run this script on an AWS EC2 instance to have the script run indefinitely.

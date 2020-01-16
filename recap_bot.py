import praw
import re
import requests
import smmry_credentials

# Create a Reddit instance using the configuration [recap-bot] from the praw.ini file
reddit = praw.Reddit('recap-bot')
subreddit = reddit.subreddit('testingground4bots')
recap_user = reddit.user.me()

keyphrase = '!recapbot '

# Check to see if the keyphrase is in any comments
for comment in subreddit.stream.comments():
    if comment.body.startswith(keyphrase) and (comment not in recap_user.saved(limit=None)): 
        print(comment.body)

        # Save the comment so the bot does not reply to it later
        comment.save()

        # Use regex to extract the link from the request
        match = re.search(r'\[.*\]\((.*)\)', comment.body)
        link = match.group(1) if match else comment.body.replace(keyphrase, '')

        # Make API call to SMMRY using API key
        params = {'SM_API_KEY': smmry_credentials.api_key, 'SM_URL': link}
        res = requests.get(url='https://api.smmry.com', params=params).json()

        # Reply to user request
        if 'sm_api_content' in res:
            comment.reply(res['sm_api_content'])
        else:
            comment.reply('Invalid request')

        print('Replied!')

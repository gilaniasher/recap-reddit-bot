import praw
import re
import requests
import smmry_credentials

# Create a Reddit instance using the configuration [recap-bot] from the praw.ini file
reddit = praw.Reddit('recap-bot')
subreddit = reddit.subreddit('testingground4bots')

keyphrase = '!recapbot '

# Check to see if the keyphrase is in any comments
for comment in subreddit.stream.comments():
    if comment.body.startswith(keyphrase):
        # Remove the keyphrase from the bot request
        match = re.search(r'\[.*\]\((.*)\)', comment.body)

        if match:
            link = match.group(1)
            
            # Make API call to SMMRY using API key
            params = {'SM_API_KEY': smmry_credentials.api_key, 'SM_URL': link}
            res = requests.get(url='https://api.smmry.com', params=params).json()

            # Reply to user request
            if 'sm_api_content' in res:
                comment.reply(res['sm_api_content'])
            else:
                comment.reply('Invalid request')

            print('Replied!')
        else:
            comment.reply('No link found in comment')
            print('Replied')

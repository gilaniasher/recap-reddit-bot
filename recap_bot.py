import praw
import re

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
            comment.reply(link)
            print('Replied!')
        else:
            comment.reply('No link found in comment')
            print('Replied')

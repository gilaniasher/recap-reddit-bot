import praw

# Create a Reddit instance using the configuration [recap-bot] from the praw.ini file
reddit = praw.Reddit('recap-bot')
subreddit = reddit.subreddit('testingground4bots')

keyphrase = '!recapbot '

# Check to see if the keyphrase is in any comments
for comment in subreddit.stream.comments():
    if comment.body.startswith(keyphrase):
        # Remove the keyphrase from the bot request
        link = comment.body[len(keyphrase):]

        # Just write this link back as a reply as a test
        comment.reply(link)

        print('Replied!')

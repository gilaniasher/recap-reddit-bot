import praw

# Create a Reddit instance using the configuration [recap-bot] from the praw.ini file
reddit = praw.Reddit('recap-bot')
subreddit = reddit.subreddit('testingground4bots')

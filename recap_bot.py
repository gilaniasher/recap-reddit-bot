import praw

# Create a Reddit instance using the configuration [recap-bot] from the praw.ini file
reddit = praw.Reddit('recap-bot')
subreddit = reddit.subreddit('testingground4bots')

for entry in subreddit.hot(limit=5):
    print("Title: ", entry.title)
    print("Text: ", entry.selftext)
    print("________________________\n")

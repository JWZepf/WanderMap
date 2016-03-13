#!/usr/bin/python
import praw

user_agent = ("WanderMap Bot 0.1")  # Sets name of User Agent that we will use

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("earthporn") # We are looking at /r/earthporn

array = []
for submission in subreddit.get_hot(limit = 25): # Get the top 25 hot posts
    array.append(submission.title)
    '''
    print ("Title: ", submission.title)
    print ("Text: ", submission.selftext)
    print ("Score: ", submission.score)
    print ("---------------------------------\n")
    '''
print (array[5])

import tweepy
import time

auth = tweepy.OAuthHandler('61dyq75hBA5sfkIksLi9wt6u9','imtPifiWNwM5x1r2Pmip75aqLDoByQZfqTTWuIVuYsbu7dawJN')

auth.set_access_token('3668518939-4bsUA8m6sAw0aapNhCV7shKqMcqA7q9BbVCNfDZ','GF7KkJZAIAGJOqhAWH4WZdJ04fjaaI0YpImosXoFVySNs')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Python'
numberOfTweets = 1000

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        print('Tweet Retweeted')
        tweet.retweet()
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
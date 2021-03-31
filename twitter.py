from auth import Auth
import tweepy
from pprint import pprint
import json

class Twitter:
    def __init__(self):
        self.client = Auth().api
    
    def tweet(self, tweet_text):
        request = self.client.update_status(tweet_text)
        print('Tweet: '+request)
    
    def search_tweet(self, search_text):
        try:
            request = self.client.search(search_text)
            for tweet in request:
                print(str(tweet.user.screen_name))
                print(str(tweet.text)+'\n')

        except tweepy.TweepError as e:
            print('Error: '+str(e.message))

        
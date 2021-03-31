from auth import Auth

class Twitter:
    def __init__(self):
        self.client = Auth().api
    
    def tweet(self, tweet_text):
        request = self.client.update_status(tweet_text)

        
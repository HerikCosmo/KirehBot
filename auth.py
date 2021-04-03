from dotenv import load_dotenv
from pprint import pprint
import tweepy
import os

class Auth:
    def __init__(self):
        load_dotenv()
        CK = os.environ.get('CONSUMER_KEY')
        CS = os.environ.get('CONSUMER_SECRET')
        TK = os.environ.get('TOKEN_KEY')
        TS = os.environ.get('TOKEN_SECRET')
        self.authenticate(CK, CS, TK, TS)

    def authenticate(self, CK, CS, TK, TS):
        self.auth = tweepy.OAuthHandler(CK, CS)
        self.auth.set_access_token(TK, TS)
        self.api = tweepy.API(self.auth)

    if __name__ == '__main__':
        print('Executar apenas no main')
        


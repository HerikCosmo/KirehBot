from auth import Auth
from time import sleep
import tweepy


class Twitter:
    def __init__(self):
        self.client = Auth().api
    
    def tweet(self, tweet_text):
        try: 
            request = self.client.update_status(tweet_text)
            print('Tweet send: '+tweet_text)
        except tweepy.TweepError as e:
            print('Error: '+str(e.message))
    
    def search_tweet(self, search_text):
        try:
            request = self.client.search(search_text)
            for tweet in request:
                print(str(tweet.user.screen_name))
                print(str(tweet.text)+'\n')

        except tweepy.TweepError as e:
            print('Error: '+str(e.message))

    def reply_tweet(self, search_text):
        try:
            request = self.client.search(search_text)
            for tweet in request:
                screen_name = tweet.user.screen_name
                id_status = tweet.id
                reply = f'@{screen_name} {search_text}'
                self.client.update_status(reply, id_status)
        except tweepy.TweepError as e:
            print('Error: '+str(e.message))

    def reply_tweet_with_image(self, search_text, image):
        try:
            print('pesquisando...')
            request = self.client.search(search_text)
            ids = open('ids.txt', 'r')
            ids_id = ids.readlines()
            
            ids.close()

            for tweet in request:
                idtxt = tweet.id_str+'\n'
                if idtxt not in ids_id:
                    screen_name = tweet.user.screen_name
                    id_status = tweet.id
                    id_image = self.image(image)
                    reply = f'@{screen_name}'
                    id_write = open('ids.txt', 'a')
                    id_write.write(str(id_status)+'\n')
                    id_write.close()
                    sleep(1)
                    self.client.update_status(reply, id_status, media_ids=[id_image])
        
        except tweepy.TweepError as e:
            print('Error: '+str(e.message))

        sleep(5)


    def image(self, image):
        try:
            request = self.client.media_upload(image)
            return request.media_id
        except tweepy.TweepError as e:
            print('Error: '+str(e.message))



        
from image_maker import ImageMaker
from auth import Auth
from time import sleep
import tweepy
from pprint import pprint

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

    def reply_tweet_with_image(self, search_text):
        try:
            print('pesquisando...')
            request = self.client.search(search_text, tweet_mode='extended') # buscar a #herikbot
            list_ids = self.manager_ids()
            image = 'result.jpg'
            for tweet in request: # para cada tweet da pesquisa
                str_id = tweet.id_str+'\n' # adpatar id para buscar
                if str_id not in list_ids: # se o id nao estiver na lista
                    screen_name = tweet.user.screen_name # pega o nome do tweet
                    ImageMaker(tweet.full_text)
                    id_status = tweet.id # id do tweet
                    id_image = self.image(image) # imagem
                    reply = f'@{screen_name}' # str da resposta
                    sleep(1)
                    self.client.create_favorite(id_status)
                    sleep(1)
                    self.client.update_status(reply, id_status, media_ids=[id_image]) # envia
                    sleep(1)
                    self.add_id(id_status)
        
        except tweepy.TweepError as e:
            print('Error: '+str(e.message))

        sleep(5)

    def manager_ids(self):
        archive = open('list_ids.txt', 'r')
        list_ids = archive.readlines()
        archive.close()
        return list_ids
        
    def add_id(self, id_status):
        archive = open('list_ids.txt', 'a')
        archive.write(str(id_status)+'\n')
        archive.close()
    
    def image(self, image):
        try:
            request = self.client.media_upload(image)
            return request.media_id
        except tweepy.TweepError as e:
            print('Error: '+str(e.message))
    
    if __name__ == '__main__':
        print('Executar apenas no main')




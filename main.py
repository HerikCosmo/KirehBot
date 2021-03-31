from twitter import Twitter
import keyboard
from time import sleep
twitter = Twitter()




def menu():
    print('='*10)
    print('BEM VINDO AO HERIK BOT')
    print('='*10)
    print('Escolha uma opção:')
    print('1. Tweetar\n2. Pesquisar Tweets\n3. Responder Tweet\n4. Automatico')
    opcao = int(input())
    funcoes(opcao)

def funcoes(opcao):
    if(opcao == 1):
        twitter.tweet(input('Tweet: '))
    elif(opcao == 2):
        twitter.search_tweet(input('Search Tweet: '))
    elif(opcao == 3):
        twitter.reply_tweet(input('Search tweet to reply: '))
    elif(opcao == 4):
        print('Modo Automático ativado. Pressione "E" para desativar')
        while True:
            try:
                twitter.reply_tweet_with_image('#herikbot', 'teste.jpeg')
                
                if keyboard.is_pressed('e'):
                    break
                
            except: 
                break
            
        
menu()
#twitter.reply_tweet_with_image('#herikbot', 'teste.jpeg')
#twitter.image('teste.jpeg')
# while True:
#     twitter.reply_tweet_with_image('#herikbot', 'teste.jpeg')
#     sleep(5)
    
from PIL import Image, ImageDraw, ImageFont
import textwrap
from numpy import random

class ImageMaker:
    def __init__(self, tweet):
        self.myFont = ImageFont.truetype('Fonts/NexaBold.otf', 50)
        self.text = self.get_text(tweet)
        self.make_image()

    def make_image(self):
        base = Image.open('Templates/base.jpg')
        character = Image.open('Source/'+self.random_character())
        background = Image.open('Templates/background.png')
        logo = Image.open('Templates/logo.png')

        base.paste(character, (0,0), character)
        base.paste(background, (0,0), background)
        base.paste(logo, (0,0), logo)
        insert_text = ImageDraw.Draw(base)
        insert_text.text((50, 50), font=self.myFont, fill=(255,255,255), text=textwrap.fill(self.text, 22))
        
        base.save('result.jpg', quality=95)
    
    def get_text(self, text):
        return text.replace('#herikbot', '').strip()
    
    def random_character(self):
        characters = ['luffy.png', 'zoro.png', 'nami.png', 'usopp.png', 'sanji.png']
        return random.choice(characters)

    if __name__ == '__main__':
        print('Executar apenas no main')

ImageMaker('ndsandsajdnsajds')
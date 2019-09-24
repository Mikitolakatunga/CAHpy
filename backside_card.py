from create_card import *
from draw_mtext import *
import os

dir = os.getcwd()

size = (230, 261)
text = "Cards Against Humanity"

# white backside
wcard = create_card(size, 'white', 'black')
##wcard = add_black_corners(wcard, 20)
font = ImageFont.truetype('consolab.ttf', 37)
wcard = write_text(10, 20, wcard, text, font, 'black')
wcard.save(f'{dir}/Back_Cards/white_back.png', optimize=True)

# Black backside
bcard = create_card(size, 'black', 'white')
##bcard = add_corners(bcard, 20)
font = ImageFont.truetype('consolab.ttf', 37)
bcard = write_text(10, 20, bcard, text, font, 'white')
bcard.save(f'{dir}/Back_Cards/black_back.png', optimize=True)

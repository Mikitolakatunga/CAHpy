from create_card import *
from draw_mtext import *

size = (230, 261)
text = "Cards Against Humanity"

# white backside
wcard = create_card(size, 'white', 'black')
wcard = add_black_corners(wcard, 20)
font = ImageFont.truetype('consolab.ttf', 37)
wcard = write_text(10, 20, wcard, text, font, 'black')
wcard.save('D:/PyProjects/CAHpy/Back_Cards/white_back.png', optimize=True)

# Black backside
bcard = create_card(size, 'black', 'white')
bcard = add_corners(bcard, 20)
font = ImageFont.truetype('consolab.ttf', 37)
bcard = write_text(10, 20, bcard, text, font, 'white')
bcard.save('D:/PyProjects/CAHpy/Back_Cards/black_back.png', optimize=True)
